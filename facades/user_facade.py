import re

from entities.error_response import ErrorResponse
from entities.messages import Message
from entities.response import Response
from errors.user_errors import (user_errors,
                                NotCorrectFormatError,
                                CreatingUserError,
                                ShortPasswordError,
                                NotLowercaseCharacter,
                                NotUppercaseCharacter,
                                NotDigitCharacter,
                                NotLowercaseCharacter,
                                NotSpecialCharacter
                                )
from logs import Logger


class UserFacade():
    def creation_validation(self, user):
        validation = self._email_validation(user.email)
        validation = validation and self._password_validation(user.password)
        return validation

    def _email_validation(self, email):
        logger = Logger('validate_email::facade::flask')
        logger.debug('Validating email format')
        result = False

        regex = r'[^@]+@[^@]+\.[^@]+'

        if re.match(regex, email):
            result = True

        return result

    def _password_validation(self, password):
        logger = Logger('validate_password::facade::flask')
        logger.debug('Validating email strength')
        result = False

        # Expresión regular que indica que el password debe:
        # 1. Tener una longitud minima de 8 caracteres
        # 2. Tener una combinación de mayúsculas y minúsculas
        # 3. Debe de intercalar letras y números
        # 4. Debe de contener, almenos un caracter no alfanumérico
        reg = r'[A-Za-z0-9@#$%^&+=]{8,}'

        if re.match(reg, password):
            result = True

        return result


user_facade = UserFacade()
