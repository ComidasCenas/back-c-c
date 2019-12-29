recipe_errors = {
    'RecipeSuccessfullyFound': {
        'message': 'The recipe has been found successfully',
        'status': 200
    },
    'RecipeCreationSuccess': {
        'message': 'The recipe has been created successfully',
        'status': 201
    },
    'NotCorrectFormatError': {
        'message': 'Name, ingredients or instructions have an incorrect format',
        'status': 400
    },
    'RecipeNotFoundError': {
        'message': 'There is no recipe with that name.',
        'status': 404
    },
    'RecipeAlreadyExistsError': {
        'message': 'A recipe with that name already exists.',
        'status': 409
    },
    'CreatingRecipeError': {
        'message': 'An error occurred while creating recipe',
        'status': 500
    },
    'GettingRecipesListError': {
        'message': 'An error occurred while getting the recipes list',
        'status': 500
    }
}


class RecipeNotFoundError(Exception):
    pass


class RecipeAlreadyExistsError(Exception):
    pass


class CreatingRecipeError(Exception):
    pass


class RecipeCreationSuccess(Exception):
    pass


class RecipeSuccessfullyFound(Exception):
    pass


class GettingRecipesListError(Exception):
    pass


class NotCorrectFormatError(Exception):
    pass
