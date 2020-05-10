import asyncio
import logging
import json
import time

import websockets
from kafka import KafkaConsumer
from websockets_server import config


async def server_handler(websocket, path):
    consumer = KafkaConsumer(
      config.FAKE_TRANSACTIONS_TOPIC,
      bootstrap_servers=config.KAFKA_BROKER_URL,
      value_deserializer=json.loads
    )

    for msg in consumer:
        payload = json.dumps(msg.value)

        await websocket.send(payload)


def main():
    server = websockets.serve(server_handler, config.HOST, config.PORT)
    event_loop = asyncio.get_event_loop()

    event_loop.run_until_complete(server)
    event_loop.run_forever()


if __name__ == "__main__":
    main()
