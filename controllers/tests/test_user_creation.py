import unittest
from unittest.mock import MagicMock

from ..user_creation import user_creation

class TestUserCreation(unittest.TestCase):
    def test_given_name_and_password_creates_a_user(self):
        email = 'an_email@test.es'
        password ='a password'
        UserClass = MagicMock()

        user_creation(email, password, UserClass)

        UserClass.have_called_with(email, password)

    def test_given_name_and_password_check_user_created(self):
