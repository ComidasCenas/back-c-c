from helpers.serializable_decorator import serializable


class Response():
    def __init__(self, status, body):
        self.status = status
        self.body = body
