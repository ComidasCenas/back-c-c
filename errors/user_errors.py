user_errors = {
    'UserCreationSuccess': {
        'message': 'The user has been crated successfully',
        'status': 201
    },
    'NotCorrectFormatError': {
        'message': 'The email or the password has an incorrect format.',
        'status': 400
    },
    'UserNotFoundError': {
        'message': 'The id does not match any user',
        'status': 404
    },
    'UserAlreadyExistsError':  {
        'message': 'A user with that email already exists.',
        'status': 409
    },
    'CreatingUserError': {
        'message': 'An error occurred while creating user',
        'status': 500
    }
}


class NotCorrectFormatError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class CreatingUserError(Exception):
    pass


class UserCreationSuccess(Exception):
    pass


class UserNotFoundError(Exception):
    pass
