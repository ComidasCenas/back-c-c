from entities.error_response import ErrorResponse
from entities.messages import Message
from entities.response import Response
from entities.user_entity import User
from errors.user_errors import (
    user_errors,
    UserNotFoundError,
    GettingUserError,
    UserFoundSucces
)
from logs import Logger
from models.user_model import UserModel


def get_user_by_id(user_id):
    logger = Logger('get_user_by_id::controller::flask')
    logger.debug('Trying to get user by id')
    try:
        user = UserModel.find_by_id(user_id)
        if not user:
            raise UserNotFoundError
        user_entity = User(user.email, user.password)
        # return Response(
        #     user_errors['UserFoundSucces']['status'],
        #     Message(
        #         f'user_id: {user_entity.id}, user_email: {user_entity.email} ')
        # )
        # # ¿Entidad?

    except UserNotFoundError:
        error_response = ErrorResponse('UserNotFoundError', 'user')
        logger.warning(f'The user with id {user_id} has not been found')
    except GettingUserError:
        error_response = ErrorResponse('GettingUserError', 'user')
        logger.warning('There was an error while getting the user')
