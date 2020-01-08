from errors.user_errors import user_errors, UserNotFoundError
from logs import Logger
from models.user_model import UserModel


def get_user_by_id(user_id):
    logger = Logger('get_user_by_id::controller::flask')
    logger.debug('Trying to get user by id')
    try:
        user = UserModel.find_by_id(user_id)
        if not user:
            raise UserNotFoundError
