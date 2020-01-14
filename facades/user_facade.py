import re

from entities.error_response import ErrorResponse
from entities.messages import Message
from entities.response import Response
from errors.user_errors import user_errors, NotCorrectFormatError
from logs import Logger


class UserFacade():
    def creation_validation(self, user):
        validation = self._email_validation(user.email)
        validation = validation and self._password_validation(user.password)
        return validation

    def _email_validation(self, email):
        logger = Logger('validate_email::facade::flask')
        logger.debug('Validating email format')

        regex = '[^@\s]+@[^@\s]+\.[^@\s]+'

        try:
            if re.match(regex, email):
                return True
        except NotCorrectFormatError:
            error_response = ErrorResponse('NotCorrectFormatError', 'user')
            logger.error('The email does not have a correct format')
            return Response(user_errors['NotCorrectFormatError']['status'],
                            Message('The email does not have a correct format'))

    def _password_validation(self, password):
        return True


user_facade = UserFacade()
