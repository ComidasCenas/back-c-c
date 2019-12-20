errors = {
    'UserAlreadyExistsError': {
        'message': 'A user with that username already exists.',
        'status': 400
    },
    'RecipeNotFoundError': {
        'message': 'There is no recipe with that name.',
        'status': 404
    },
    'RecipeAlreadyExistsError': {
        'message': 'A recipe with that name already exists.',
        'status': 400
    },
    'CreatingRecipeError': {
        'message': 'An error occurred while creating recipe',
        'status': 500
    }
}


class UserAlreadyExistsError(Exception):
    pass


class RecipeNotFoundError(Exception):
    pass


class RecipeAlreadyExistsError(Exception):
    pass


class CreatingRecipeError(Exception):
    pass
