from entities.error_response import ErrorResponse
from entities.messages import Message
from entities.recipe_entity import Recipe
from entities.response import Response
from errors.recipe_errors import recipe_errors, RecipeAlreadyExistsError, RecipeCreationSuccess, CreatingRecipeError, NotCorrectFormatError
from facades.recipe_facade import recipe_facade
from models.recipe_model import RecipeModel
from logs import Logger


def recipe_creation(name, ingredients, instructions):
    logger = Logger('recipe_creation::controller::flask')
    logger.debug('Creating recipe')
    try:
        recipe = Recipe(name, ingredients, instructions)

        if not recipe_facade.recipe_creation_validation(recipe):
            raise NotCorrectFormatError
        if RecipeModel.find_by_name(name):
            raise RecipeAlreadyExistsError

        recipe = RecipeModel(name, ingredients, instructions)

        recipe.save()
        return Response(recipe_errors['RecipeCreationSuccess']['status'], Message(recipe_errors['RecipeCreationSuccess']['message']).to_json())
    except NotCorrectFormatError:
        error_response = ErrorResponse('NotCorrectFormatError', 'recipe')
        logger.warning('The recipe has an incorrect format')
    except RecipeAlreadyExistsError:
        error_response = ErrorResponse('RecipeAlreadyExistsError', 'recipe')
        logger.warning('Recipe already exists')
        return Response(error_response.code, error_response.to_json())
    except CreatingRecipeError:
        error_response = ErrorResponse('CreatingRecipeError', 'recipe')
        logger.warning('Error creating recipe')
        return Response(error_response.code, error_response.to_json())
