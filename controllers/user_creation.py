from models.user_model import UserModel
from entities.response import Response
from entities.messages import Message
from entities.error_response import ErrorResponse
from errors.user_errors import user_errors, UserAlreadyExistsError, NotCorrectFormatError, CreatingUserError
from facades.user_facade import user_facade
from entities.user_entity import User
from logs import Logger


def user_creation(email, password):
    logger = Logger('user_creation::controller::flask')
    logger.debug('Creating user')
    try:
        user = User(email, password)

        if not user_facade.creation_validation(user):
            raise NotCorrectFormatError
        if UserModel.find_by_email(email):
            raise UserAlreadyExistsError

        user = UserModel(email, password)

        user.save()
        return Response(user_errors['UserCreationSuccess']['status'], Message(user_errors['UserCreationSuccess']['message']).to_json())
    except UserAlreadyExistsError:
        error_response = ErrorResponse('UserAlreadyExistsError', 'user')
        logger.warning('User already exists')
        return Response(error_response.code, error_response.to_json())
    except NotCorrectFormatError:
        error_response = ErrorResponse('NotCorrectFormatError', 'user')
        logger.error('Incorrect format')
        return Response(error_response.code, error_response.to_json())
    except:
        error_response = ErrorResponse('CreatingUserError', 'user')
        logger.error('Database error')
        return Response(error_response.code, error_response.to_json())
