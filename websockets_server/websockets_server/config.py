import os


def _get_env_variable(key: str) -> str:
    value = os.getenv(key)

    if value is None:
        raise ConfigException()

    return value

HOST = _get_env_variable("HOST")

PORT = _get_env_variable("PORT")

KAFKA_BROKER_URL = _get_env_variable('KAFKA_BROKER_URL')

REAL_TRANSACTIONS_TOPIC = _get_env_variable('REAL_TRANSACTIONS_TOPIC')

FAKE_TRANSACTIONS_TOPIC = _get_env_variable('FAKE_TRANSACTIONS_TOPIC')