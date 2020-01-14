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

        regex = '[^@\s]+@[^@\s]+\.[^@\s]+'

        try:
            if re.match(regex, email):
                return True
        except NotCorrectFormatError:
            error_response = ErrorResponse('NotCorrectFormatError', 'user')
            logger.error('The email does not have a correct format')
            return Response(error_response.code, error_response)

        except Exception:
            error_response = ErrorResponse('CreatingUserError', 'user')
            logger.error('An error occurred while validating the email')
            return Response(error_response.code, error_response)

    def _password_validation(self, password):
        logger = Logger('validate_password::facade::flask')
        logger.debug('Validating email strength')

        char_regex = re.compile(r'(\w{8,})')
        lower_regex = re.compile(r'[a-z]+')
        upper_regex = re.compile(r'[A-Z]+')
        digit_regex = re.compile(r'[0-9]+')
        special_regex = re.compile(r'[ !@£$%^&*()_+={}?:~[]]+]')

        try:
            if char_regex.findall(password) == list():
                raise ShortPasswordError
            if lower_regex.findall(password) == list():
                raise NotLowercaseCharacter
            if upper_regex.findall(password) == list():
                raise NotUppercaseCharacter
            if digit_regex.findall(password) == list():
                raise NotDigitCharacter
            if special_regex.findall(password) == list():
                raise NotSpecialCharacter
            return True
        except ShortPasswordError:
            error_response = ErrorResponse('ShortPasswordError', 'user')
            logger.error('The password has less than 8 characters')
            return Response(error_response.code, error_response)
        except NotLowercaseCharacter:
            error_response = ErrorResponse('NotLowercaseCharacter', 'user')
            logger.error('There are no lowercase characters in the password')
            return Response(error_response.code, error_response)
        except NotUppercaseCharacter:
            error_response = ErrorResponse('NotUppercaseCharacter', 'user')
            logger.error('There are no uppercase characters in the password')
            return Response(error_response.code, error_response)
        except NotDigitCharacter:
            error_response = ErrorResponse('NotDigitCharacter', 'user')
            logger.error('There are no digit characters in the password')
            return Response(error_response.code, error_response)
        except NotSpecialCharacter:
            error_response = ErrorResponse('NotSpecialCharacter', 'user')
            logger.error('There are no special characters in the password')
            return Response(error_response.code, error_response)


user_facade = UserFacade()
