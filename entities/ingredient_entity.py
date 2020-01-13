from helpers.serializable_decorator import serializable


@serializable
class IngredientEntity():
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
