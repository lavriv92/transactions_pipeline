import os
import json
from kafka import KafkaConsumer

from transactions_analyzator import config
from transactions_analyzator.analyzator import is_fake


def main():
    consumer = KafkaConsumer(
        config.TRANSACTIONS_TOPIC,
        value_deserializer=json.loads,
        bootstrap_servers=config.KAFKA_BROKER_URL
    )

    for msg in consumer:
        t_type = 'fake' if is_fake(msg.value) else 'real'
        print(f"{t_type}: {msg.value}")


if __name__ == "__main__":
    main()