import asyncio
import logging
import json
import time

import websockets
from kafka import KafkaConsumer
from . import config


async def _server_handler(websocket, path):
    consumer = KafkaConsumer(
      config.FAKE_TRANSACTIONS_TOPIC,
      bootstrap_servers=config.KAFKA_BROKER_URL,
      value_deserializer=json.loads
    )

    for msg in consumer:
        payload = json.dumps(msg.value)

        await websocket.send(payload)


def start_server():
    server = websockets.serve(_server_handler, config.HOST, config.PORT)
    event_loop = asyncio.get_event_loop()

    event_loop.run_until_complete(server)
    event_loop.run_forever()