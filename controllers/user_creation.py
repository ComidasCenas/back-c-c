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
        return Response(user_errors['UserCreationSuccess']['status'], Message(user_errors['UserCreationSuccess']['message']).toJson())
    except UserAlreadyExistsError:
        errorResponse = ErrorResponse('UserAlreadyExistsError')
        logger.warning('User already exists')
        return Response(errorResponse.code, errorResponse.toJson())
    except NotCorrectFormatError:
        errorResponse = ErrorResponse('NotCorrectFormatError')
        logger.error('Incorrect format')
        return Response(errorResponse.code, errorResponse.toJson())
    except:
        errorResponse = ErrorResponse('CreatingUserError')
        logger.error('Database error')
        return Response(errorResponse.code, errorResponse.toJson())
