import asyncio
import logging
import json
import time

import websockets
from kafka import KafkaConsumer
from websockets_server import config

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


async def server_handler(websocket, path):
    # real_consumer = KafkaConsumer(
    #   config.REAL_TRANSACTIONS_TOPIC,
    #   bootstrap_servers=config.KAFKA_BROKER_URL,
    #   value_deserializer=json.loads
    # )

    # fake_consumer = KafkaConsumer(
    #   config.FAKE_TRANSACTIONS_TOPIC,
    #   bootstrap_servers=config.KAFKA_BROKER_URL,
    #   value_deserializer=json.loads
    # )

    # for msg in real_consumer:
    #     await websocket.send(msg.value)

    # for msg in fake_consumer:
    #     await websocket.send(msg.value)

    while True:
      await websocket.send({ 'message': 'Hello' })
      time.sleep(3)


def main():
    logger.info("Start socket server")
    server = websockets.serve(server_handler, "0.0.0.0", 3000)

    event_loop = asyncio.get_event_loop()

    event_loop.run_until_complete(server)
    event_loop.run_forever()


if __name__ == "__main__":
    main()
