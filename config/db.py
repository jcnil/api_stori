import os

from mongoengine import connect


def connect_db() -> None:
    """
    :return: connect mongodb
    """
    return connect(
        host=os.getenv("MONGO_URI")
    )
