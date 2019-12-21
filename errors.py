errors = {
    'UserAlreadyExistsError':  {
        'message': 'A user with that email already exists.',
        'status': 409
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
    'CreatingUserError': {
        'message': 'An error occurred while creating user',
        'status': 500
    },
    'NotCorrectFormatError': {
        'message': 'The email or the password has an incorrect format.',
        'status': 400
    },
    'UserCreationSuccess': {
        'message': 'The user has been crated successfully',
        'status': 201
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

class CreatingUserError(Exception):
    pass

class NotCorrectFormatError(Exception):
    pass


