import asyncio
import logging
import json
import time

import websockets
from kafka import KafkaConsumer
from websockets_server import config

logger = logging.getLogger(__name__)


async def server_handler(websocket, path):
    consumer = KafkaConsumer(
      config.FAKE_TRANSACTIONS_TOPIC,
      bootstrap_servers=config.KAFKA_BROKER_URL,
      value_deserializer=json.loads
    )

    for msg in consumer:
        print(msg.value)

        payload = json.dumps(msg.value)

        await websocket.send(payload)


def main():
    logger.info("Start socket server")
    server = websockets.serve(server_handler, "0.0.0.0", 3000)

    event_loop = asyncio.get_event_loop()

    event_loop.run_until_complete(server)
    event_loop.run_forever()


if __name__ == "__main__":
    main()
