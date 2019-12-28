import json


class Message():
    def __init__(self, message):
        self.message = message

    def to_json(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
