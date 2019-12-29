from entities.error_response import ErrorResponse
from entities.messages import Message
from entities.recipe_entity import Recipe
from entities.response import Response
from models.recipe_model import RecipeModel
from errors.recipe_errors import recipe_errors, RecipeNotFoundError, RecipeSuccessfullyFound
from logs import Logger


def recipe_reading(name):
    logger = Logger('recipe_reading::controller::flask')
    logger.debug('Reading recipe')
    try:
        recipe = RecipeModel.find_by_name(name)
        return Recipe(recipe.name, recipe.ingredients, recipe.instructions).to_json()
    except RecipeNotFoundError:
        error_response = ErrorResponse('RecipeNotFoundError', 'recipe')
        logger.error('Recipe not found')
        return Response(error_response.code, error_response.to_json())
