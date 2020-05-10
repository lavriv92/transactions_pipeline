import json
import os
import time

from kafka import KafkaProducer

from . import config
from .transactions import generate_fake


def start_generator():
    producer = KafkaProducer(
      bootstrap_servers=config.KAFKA_BROKER_URL,
      value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    for transaction in generate_fake():
        producer.send(config.TRANSACTIONS_TOPIC, transaction)
        time.sleep(3)