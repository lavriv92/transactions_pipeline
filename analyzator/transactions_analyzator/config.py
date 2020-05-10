import os

from .exceptions import ConfigException

def _get_env_variable(key):
    value = os.getenv(key)

    if value is None:
        raise ConfigException()

    return value


KAFKA_BROKER_URL = _get_env_variable('KAFKA_BROKER_URL')

TRANSACTIONS_TOPIC = _get_env_variable('TRANSACTIONS_TOPIC')