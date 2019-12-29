import json


class Ingredients():
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def to_json(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
