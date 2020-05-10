import json
import os
import time

from kafka import KafkaProducer

from transactions_generator import config
from transactions_generator.transactions import generate_fake


def main():
    producer = KafkaProducer(
      bootstrap_servers=config.KAFKA_BROKER_URL,
      value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    for transaction in generate_fake():
        producer.send(config.TRANSACTIONS_TOPIC, transaction)
        time.sleep(3)


if __name__ == '__main__':
    main()
