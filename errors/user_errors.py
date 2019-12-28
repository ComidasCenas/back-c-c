user_errors = {
    'UserCreationSuccess': {
        'message': 'The user has been created successfully',
        'status': 201
    },
    'NotCorrectFormatError': {
        'message': 'The email or the password has an incorrect format.',
        'status': 400
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
