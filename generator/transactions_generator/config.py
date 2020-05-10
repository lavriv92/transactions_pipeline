import os

from .exceptions import ConfigException

def _get_env_value(key: str) -> str:
    value = os.getenv(key)

    if value is None:
        raise ConfigException(f'env variable {key} is missing')

    return value


KAFKA_BROKER_URL = _get_env_value("KAFKA_BROKER_URL")

TRANSACTIONS_TOPIC = _get_env_value('TRANSACTIONS_TOPIC')