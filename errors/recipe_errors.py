recipe_errors = {
    'RecipeCreationSuccess': {
        'message': 'The recipe has been crated successfully',
        'status': 201
    },
    'NotCorrectFormatError': {
        'message': 'The recipe has an incorrect format.',
        'status': 400
    },
    'RecipeDoesNotExist': {
        'message': 'This recipe does not exist.',
        'status': 404
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
    }
}


class RecipeCreationSuccess(Exception):
    pass


class NotCorrectFormatError(Exception):
    pass


class RecipeDoesNotExist(Exception):
    pass


class RecipeNotFoundError(Exception):
    pass


class RecipeAlreadyExistsError(Exception):
    pass


class CreatingRecipeError(Exception):
    pass
