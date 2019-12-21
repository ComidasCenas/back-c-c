from models.user_model import UserModel
from entities.response import Response
from entities.messages import Message
from entities.error_response import ErrorResponse
from errors import errors, UserAlreadyExistsError, NotCorrectFormatError, CreatingUserError
from facades.user_facade import user_facade
from entities.user_entity import User


def user_creation(email, password):
    try:
        user = User(email, password)

        if not user_facade.creation_validation(user):
            raise NotCorrectFormatError
        if UserModel.find_by_email(email):
            raise UserAlreadyExistsError

        user = UserModel(email, password)

        user.save()
        return Response(errors['UserCreationSuccess']['status'], Message(errors['UserCreationSuccess']['message']).toJson())
    except UserAlreadyExistsError:
        errorResponse = ErrorResponse('UserAlreadyExistsError')
        return Response(errorResponse.code, errorResponse.toJson())
    except NotCorrectFormatError:
        errorResponse = ErrorResponse('NotCorrectFormatError')
        return Response(errorResponse.code, errorResponse.toJson())
    except:
        errorResponse = ErrorResponse('CreatingUserError')
        return Response(errorResponse.code, errorResponse.toJson())
