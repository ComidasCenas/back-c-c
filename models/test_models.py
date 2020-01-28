# constructor, save, find by email, find by id, delete user, repr
import unittest

from models.user_model import UserModel


class TestUserModel(unittest.TestCase):
    def test_constructor_function(self):

        user = UserModel('anemail@whatever.com', 'NiChurrasNiMerinas')

        self.assertEqual(True, isinstance(user, UserModel))
        self.assertEqual(user.email, 'anemail@whatever.com')
        self.assertEqual(user.password, 'NiChurrasNiMerinas')
