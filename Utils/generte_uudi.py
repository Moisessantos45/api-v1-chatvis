from uuid import uuid4


def generate_id(length=10):
    uniqued_id = uuid4().hex
    return uniqued_id[:length]
