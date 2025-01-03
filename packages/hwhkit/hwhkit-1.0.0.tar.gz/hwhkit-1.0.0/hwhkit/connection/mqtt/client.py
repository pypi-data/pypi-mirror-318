import paho.mqtt.client as mqtt
import asyncio
import functools
from typing import Callable, Any, Dict, List


class MQTTAsyncClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, broker: str = None, port: int = None, client_id: str = None, username: str = None, password: str = None):
        if not self._initialized:
            self.broker = broker
            self.port = port
            self.client_id = client_id
            self.client = mqtt.Client(client_id=client_id)
            if username and password:
                self.client.username_pw_set(username, password)
            self.client.on_connect = self.on_connect
            self.client.on_disconnect = self.on_disconnect
            self.client.reconnect_delay_set(min_delay=1, max_delay=120)
            self._callbacks: Dict[str, List[Callable[[str], Any]]] = {}
            self._initialized = True
            self.loop = asyncio.get_event_loop()

    def on_connect(self, client: mqtt.Client, userdata: Any, flags: dict, rc: int):
        if rc == 0:
            print("Connected to MQTT Broker!")
            for topic in self._callbacks.keys():
                client.subscribe(topic)
        else:
            print(f"Failed to connect, return code {rc}")

    def on_disconnect(self, client: mqtt.Client, userdata: Any, rc: int):
        print("Disconnected from MQTT Broker!")
        if rc != 0:
            print(f"Unexpected disconnection. Reconnecting...")

    def start(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()

    def subscribe(self, topic: str, callback: Callable[[str], Any]):
        if topic not in self._callbacks:
            self._callbacks[topic] = []
        self._callbacks[topic].append(callback)
        self.client.message_callback_add(topic, lambda client, userdata, msg: self._on_message(topic, msg))
        print(f"Subscribed to topic: {topic}")

    def _on_message(self, topic: str, msg: mqtt.MQTTMessage):
        print(f"Received message from topic: {topic}")
        for callback in self._callbacks.get(topic, []):
            asyncio.run_coroutine_threadsafe(callback(msg.payload.decode('utf-8')), self.loop)

    def publish(self, topic: str, message: str, qos: int = 0, retain: bool = False):
        result = self.client.publish(topic, message, qos=qos, retain=retain)
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Message published to {topic}")
        else:
            print(f"Failed to publish message to {topic}, error code: {result.rc}")


def mqtt_subscribe(topic: str):
    def decorator(func: Callable[[str], Any]):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        client = MQTTAsyncClient()
        client.subscribe(topic, wrapper)
        return wrapper

    return decorator