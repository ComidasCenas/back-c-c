from entities.ingredient_entity import IngredientEntity
from helpers.serializable_decorator import serializable


@serializable
class Recipe():
    def __init__(self, recipe_post, user_id):
        self.name = recipe_post['name']
        self.ingredients = list()
        self.user = user_id
        for ingredint_dic in recipe_post['ingredients']:
            self.ingredients.append(IngredientEntity(**ingredint_dic))

        self.instructions = recipe_post['recipeSteps']
        self.photo = recipe_post['photo']

        if ('relatedRecipes' not in recipe_post):
            self.recipes_related = list()
        else:
            self.recipes_related = recipe_post['relatedRecipes']
