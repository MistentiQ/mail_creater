import uuid


def new_password() -> str:

    return uuid.uuid4().hex[0:8]


PASSWORD = new_password()
