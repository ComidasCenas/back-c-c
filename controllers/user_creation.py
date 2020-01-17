import traceback
from models.user_model import UserModel
from entities.response import Response
from entities.messages import Message
from entities.error_response import ErrorResponse
from errors.user_errors import user_errors, UserAlreadyExistsError
from errors.user_errors import NotCorrectFormatError, CreatingUserError
from facades.user_facade import user_facade
from logs import Logger


def user_creation(email, password, User):
    logger = Logger('user_creation::controller::flask')
    logger.debug('Creating user')
    try:
        logger.debug('Instantiating user entity')
        user = User(email, password)

        logger.debug('Validating')
        if not user_facade.creation_validation(user):
            raise NotCorrectFormatError

        logger.debug('Searching email')
        if UserModel.find_by_email(email):
            raise UserAlreadyExistsError

        logger.debug('Instantiating user model')
        user = UserModel(email, password)

        logger.debug('Saving user')
        user.save()
        return Response(
            user_errors['UserCreationSuccess']['status'],
            Message(user_errors['UserCreationSuccess']['message'])
        )
    except UserAlreadyExistsError:
        error_response = ErrorResponse('UserAlreadyExistsError', 'user')
        logger.warning('User already exists')
        return Response(error_response.code, error_response)
    except NotCorrectFormatError:
        error_response = ErrorResponse('NotCorrectFormatError', 'user')
        logger.error('Incorrect format')
        return Response(error_response.code, error_response)
    except Exception:
        stacktrace = traceback.format_exc()
        error_response = ErrorResponse('CreatingUserError', 'user')
        logger.error('Error: ' + stacktrace)
        return Response(error_response.code, error_response)
