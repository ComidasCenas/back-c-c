import unittest
from unittest.mock import patch, MagicMock
from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.user_model import UserModel
from models.recipe_model import RecipeModel
from models.ingredients_recipes_model import IngredientsRecipesModel
from models.ingredients_model import IngredientsModel
from db import db
from logs import Logger


class TestUserModel(unittest.TestCase):

    email = 'pepe@mail.com'
    password = '1234'

    def create_test_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.init_app(app)
        app.app_context().push()

    def setUp(self):
        self.create_test_app()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_creation(self):
        db.session.add(UserModel(self.email, self.password))
        db.session.commit()
        result = db.session.query(UserModel).all()
        self.assertEqual(result[0].email, self.email)
        self.assertEqual(result[0].password, self.password)

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.session.add', autospec=True)
    @patch('db.db.session.commit', autospec=True)
    def test_user_save(self, mock_commit, mock_add, mock_debug):
        user_model = UserModel(self.email, self.password)
        user_model.save()

        self.assertEqual(
            mock_debug.call_args[0][1],
            'Starting save user in database'
        )
        user_saved = mock_add.call_args[0][0]

        self.assertEqual(
            user_saved.email,
            self.email
        )
        self.assertEqual(
            user_saved.password,
            self.password
        )
        self.assertEqual(
            mock_commit.call_count,
            1
        )

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.Query.filter_by', autospec=True)
    @patch('db.db.Query.first', autospec=True)
    def test_user_find_by_email(self, mock_first, mock_filter_by, mock_debug):
        class mock_query_first():
            def first(self):
                mock_first.call_count = 1

        mock_filter_by.return_value = mock_query_first()
        user_model = UserModel(self.email, self.password)
        user_model.find_by_email(self.email)

        self.assertEqual(mock_debug.call_args[0][1], 'Searching user by email')

        self.assertEqual(mock_filter_by.call_args[1]['email'], self.email)

        self.assertEqual(mock_first.call_count, 1)

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.Query.filter_by', autospec=True)
    @patch('db.db.Query.first', autospec=True)
    def test_user_find_by_id(self, mock_first, mock_filter_by, mock_debug):
        class mock_query_first():
            def first(self):
                mock_first.call_count = 1

        mock_filter_by.return_value = mock_query_first()
        user_model = UserModel(self.email, self.password)
        user_model.find_by_id(user_model.id)

        self.assertEqual(mock_debug.call_args[0][1], 'Searching user by id')

        self.assertEqual(mock_filter_by.call_args[1]['id'], user_model.id)

        self.assertEqual(mock_first.call_count, 1)

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.session.delete', autospec=True)
    @patch('db.db.session.commit', autospec=True)
    def test_user_deletion(self, mocked_commit, mocked_deletion, mocked_debug):
        user_model = UserModel(self.email, self.password)
        user_model.delete_user()

        self.assertEqual(mocked_debug.call_args[0][1], 'Deleting item')

        user_deleted = mocked_deletion.call_args[0][0]

        self.assertEqual(mocked_commit.call_count, 1)
