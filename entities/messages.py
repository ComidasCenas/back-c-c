from helpers.serializable_decorator import serializable


@serializable
class Message():
    def __init__(self, message):
        self.message = message
