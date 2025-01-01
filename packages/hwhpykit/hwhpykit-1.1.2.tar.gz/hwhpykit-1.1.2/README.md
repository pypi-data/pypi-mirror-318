
# hwhpykit
- 封装的常用第三方库
  - Mqtt

## Main function

### Connection

#### Mqtt

```
from hwhpykit.connection.mqtt import MQTTAsyncClient, mqtt_subscribe
import asyncio

# 配置 MQTT 客户端
client = MQTTAsyncClient(broker="broker.hivemq.com", port=1883, client_id="my_client")
client.start()

# 订阅主题 1
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
        asyncio.sleep(3600)  # 保持脚本运行
    )

if __name__ == '__main__':
    asyncio.run(main())

```




