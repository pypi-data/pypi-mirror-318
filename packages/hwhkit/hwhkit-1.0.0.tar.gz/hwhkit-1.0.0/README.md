
# hwhkit

## Main function
+ Connection
  + mqtt
+ llm
  
### Connection

#### Mqtt

```
from hwhkit import MQTTAsyncClient, mqtt_subscribe
import asyncio

# Config MQTT Client
client = MQTTAsyncClient(broker="broker.hivemq.com", port=1883, client_id="my_client")
client.start()


@mqtt_subscribe("topic/test1")
async def handle_message_1(message: str):
    print(f"Received message from topic 1: {message}")

@mqtt_subscribe("topic/test2")
async def handle_message_2(message: str):
    print(f"Received message from topic 2: {message}")

async def send_messages():
    while True:
        await asyncio.sleep(2)
        client.publish("topic/test1", "Hello from topic 1!")
        client.publish("topic/test2", "Hello from topic 2!")

async def main():
    await asyncio.gather(
        send_messages(),
        asyncio.sleep(3600) 
    )

if __name__ == '__main__':
    asyncio.run(main())

```

### llm

#### Three steps to use models

1. llm_config.yaml

```yaml
models:
  gpt-4o:
    name: "gpt-4o"
    short_name: "OIG4"
    company: "openai"
    max_input_token: 8100
    max_output_token: 2048
    top_p: 0.5
    top_k: 1
    temperature: 0.5
    input_token_fee_pm: 30.0
    output_token_fee_pm: 60.0
    train_token_fee_pm: 0.0
    keys:
      - name: "openai_key1"
      - name: "openai_key2"

```

2. llm_keys.yaml
```yaml
keys:
  openai_key1: "xx"
  openai_key2: "xx"
  anthropic_key1: "your_anthropic_api_key_1"
  anthropic_key2: "your_anthropic_api_key_2"
```

3. code
```python
from hwhkit.llm.config import load_models_from_config


async def main():
    models = load_models_from_config(config_file="llm_config.yaml", keys_file="llm_keys.yaml")
    print(models.list_models())

    resp = await models.get_model_instance("gpt-4o").chat("who r u?")
    print(resp)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
```
