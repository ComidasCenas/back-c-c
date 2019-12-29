import json


class Recipe():
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def to_json(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
