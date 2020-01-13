from helpers.serializable_decorator import serializable


@serializable
class IngredientRecipe():
    def __init__(self, quantity, recipe_id, name):
        self.quantity = quantity
        self.recipe_id = recipe_id
        self.name = name
