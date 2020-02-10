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


class TestUserModel (unittest.TestCase):

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
    def test_user_save(self, mockCommit, mockAdd, mockDebug):
        userModel = UserModel(self.email, self.password)
        userModel.save()

        self.assertEqual(
            mockDebug.call_args[0][1],
            'Starting save user in database'
        )
        userSaved = mockAdd.call_args[0][0]

        self.assertEqual(
            userSaved.email,
            self.email
        )
        self.assertEqual(
            userSaved.password,
            self.password
        )
        self.assertEqual(
            mockCommit.call_count,
            1
        )

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.Query.filter_by', autospec=True)
    @patch('db.db.Query.first', autospec=True)
    def test_user_find_by_email(self, mockFirst, mockFilterBy, mockDebug):
        class MockQueryFirst():
            def first(self):
                mockFirst.call_count = 1

        mockFilterBy.return_value = MockQueryFirst()
        userModel = UserModel(self.email, self.password)
        userModel.find_by_email(self.email)

        self.assertEqual(mockDebug.call_args[0][1], 'Searching user by email')

        self.assertEqual(mockFilterBy.call_args[1]['email'], self.email)

        self.assertEqual(mockFirst.call_count, 1)
