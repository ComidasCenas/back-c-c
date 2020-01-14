user_errors = {
    'UserFoundSucces': {
        'message': 'User succesfully found',
        'status': 200
    },
    'UserCreationSuccess': {
        'message': 'The user has been created successfully',
        'status': 201
    },
    'NotCorrectFormatError': {
        'message': 'The email or the password has an incorrect format.',
        'status': 400
    },
    'ShortPasswordError': {
        'message': 'The password must have at least 8 characters',
        'status': 400
    },
    'NotLowercaseCharacter': {
        'message': 'Password must contain at least one lowercase character',
        'status': 400
    },
    'NotUppercaseCharacter': {
        'message': 'Password must contain at least one uppercase character',
        'status': 400
    },
    'NotDigitCharacter': {
        'message': 'Password must contain at least one digit character',
        'status': 400
    },
    'NotSpecialCharacter': {
        'message': 'Password must contain at least one special character',
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
    },
    'GettingUserError': {
        'message': 'An error occurred while getting user',
        'status': 500
    }
}


class NotSpecialCharacter(Exception):
    pass


class NotDigitCharacter(Exception):
    pass


class NotUppercaseCharacter(Exception):
    pass


class NotLowercaseCharacter(Exception):
    pass


class ShortPasswordError(Exception):
    pass


class UserFoundSucces(Exception):
    pass


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


class GettingUserError(Exception):
    pass
