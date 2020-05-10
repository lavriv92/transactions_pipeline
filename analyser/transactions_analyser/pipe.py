import os
import json
from kafka import KafkaConsumer, KafkaProducer

from . import config
from .analyser import is_fake


def run():
    consumer = KafkaConsumer(
        config.TRANSACTIONS_TOPIC,
        value_deserializer=json.loads,
        bootstrap_servers=config.KAFKA_BROKER_URL
    )

    producer = KafkaProducer(
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        bootstrap_servers=config.KAFKA_BROKER_URL
    )

    for msg in consumer:
        if is_fake(msg.value):
            producer.send(config.FAKE_TRANSACTIONS_TOPIC, msg.value)