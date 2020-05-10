import os

from .exceptions import ConfigException

def _get_env_variable(key: str) -> str:
    value = os.getenv(key)

    if value is None:
        raise ConfigException()

    return value


KAFKA_BROKER_URL = _get_env_variable('KAFKA_BROKER_URL')

TRANSACTIONS_TOPIC = _get_env_variable('TRANSACTIONS_TOPIC')

REAL_TRANSACTIONS_TOPIC = _get_env_variable('REAL_TRANSACTIONS_TOPIC')

FAKE_TRANSACTIONS_TOPIC = _get_env_variable('FAKE_TRANSACTIONS_TOPIC')