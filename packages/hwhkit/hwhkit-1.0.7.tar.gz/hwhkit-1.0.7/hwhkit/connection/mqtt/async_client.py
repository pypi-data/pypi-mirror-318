import asyncio
import uuid
from typing import Dict, Optional, Callable, Any, List
from aiomqtt import Client, MqttError
from hwhkit.utils import logger
from hwhkit.connection.mqtt.plugins.encryption import EncryptionPlugin
from hwhkit.connection.mqtt.plugins.proto import ProtobufPlugin


class MQTTClientManager:
    def __init__(self, add_plugins=True, mqtt_config="mqtt_key_pairs.yaml"):
        self.clients: Dict[str, Client] = {}
        self.topic_callbacks: Dict[str, List[Callable[[Client, Any, str, bytes], Any]]] = {}
        self.plugins = []
        self.client_tasks: Dict[str, asyncio.Task] = {}

        if add_plugins:
            # self.plugins.append(ProtobufPlugin())
            self.plugins.append(EncryptionPlugin(mqtt_config))
            self.reversed_plugins = list(reversed(self.plugins))

    async def create_client(
        self,
        client_id: str,
        broker: str,
        port: int = 1883,
        username: Optional[str] = None,
        password: Optional[str] = None,
        keepalive: int = 60
    ) -> 'MQTTClientManager':
        if client_id in self.clients:
            raise ValueError(f"Client with ID {client_id} already exists.")

        unique_id = f"{client_id}:{uuid.uuid4().hex[:6]}"
        client = Client(
            identifier=unique_id,
            hostname=broker,
            port=port,
            username=username,
            password=password,
            keepalive=keepalive
        )

        self.clients[client_id] = client
        self.client_tasks[client_id] = asyncio.create_task(self._run_client(client, client_id))
        return self

    async def _run_client(self, client: Client, client_id: str):
        reconnect_interval = 5  # seconds
        while True:
            try:
                async with client:
                    logger.info(f"Client {client_id} connected successfully.")
                    await self._subscribe_to_topics(client, client_id)
                    await self._listen_messages(client, client_id)
            except MqttError as e:
                logger.error(f"Error with client {client_id}: {e}")
                logger.info(f"Reconnecting in {reconnect_interval} seconds...")
                await asyncio.sleep(reconnect_interval)
            except asyncio.CancelledError:
                logger.info(f"Client {client_id} task cancelled.")
                break

    async def _subscribe_to_topics(self, client: Client, client_id: str):
        for topic in self.topic_callbacks.keys():
            try:
                await client.subscribe(topic)
                logger.info(f"Client {client_id} subscribed to topic: {topic}")
            except MqttError as e:
                logger.error(f"Failed to subscribe to topic {topic} for client {client_id}: {e}")

    async def _listen_messages(self, client: Client, client_id: str):
        async for message in client.messages:
            logger.info(f"Received【{message.topic}】 size: {message.payload}")
            await self._process_message(client, str(message.topic), message.payload)

    async def _process_message(self, client: Client, topic: str, payload: bytes):
        if self.topic_callbacks.get(topic):
            processed_message = payload
            for plugin in self.reversed_plugins:
                processed_message = plugin.on_message_received(topic, processed_message)
            for callback in self.topic_callbacks[topic]:
                try:
                    await callback(client, None, topic, processed_message)
                except Exception as e:
                    logger.error(f"Error in callback for topic {topic}: {e}")

    def add_topic_handler(self, topic: str, callback: Callable[[Client, Any, str, bytes], Any]):
        if topic not in self.topic_callbacks:
            self.topic_callbacks[topic] = []
        self.topic_callbacks[topic].append(callback)
        logger.info(f"Added handler for topic: {topic}")

    async def publish(self, client_id: str, topic: str, message: str, qos: int = 0, retain: bool = False):
        client = self.clients.get(client_id)
        if client:
            processed_message = message
            for plugin in self.plugins:
                processed_message = plugin.on_message_published(topic, processed_message)

            try:
                await client.publish(topic, processed_message.encode(), qos=qos, retain=retain)
                logger.info(f"Client {client_id} published message to {topic}")
            except MqttError as e:
                logger.error(f"Client {client_id} failed to publish message to {topic}: {e}")
        else:
            raise ValueError(f"Client with ID {client_id} not found.")

    async def run(self):
        try:
            await asyncio.gather(*self.client_tasks.values())
        except asyncio.CancelledError:
            logger.info("MQTT client manager is shutting down...")
        finally:
            await self.disconnect_all()

    async def disconnect_all(self):
        for client_id, task in self.client_tasks.items():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
            logger.info(f"Disconnected client {client_id}")