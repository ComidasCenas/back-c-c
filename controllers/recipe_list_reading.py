from errors.recipe_errors import GettingRecipesListError
from logs import Logger
from models.recipe_model import RecipeModel


def recipe_list_reading():
    logger = Logger('recipe_list_reading::controller::flask')
    logger.debug('Reading recipes list')
    try:
        recipes_list = RecipeModel.get_recipes_list()
    except GettingRecipesListError:
        error_response = ErrorResponse('GettingRecipesListError', 'recipe')
        logger.error('Recipes list not found')
        return Response(error_response.code, error_response.to_json())
