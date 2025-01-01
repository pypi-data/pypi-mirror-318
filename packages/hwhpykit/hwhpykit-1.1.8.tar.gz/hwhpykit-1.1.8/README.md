
# hwhpykit

## Main function
+ Connection
  + mqtt

### Connection

#### Mqtt

```
from hwhpykit import MQTTAsyncClient, mqtt_subscribe
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




