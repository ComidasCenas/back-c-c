import unittest
from unittest.mock import patch, MagicMock

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.user_model import UserModel
from models.recipe_model import RecipeModel
from models.ingredients_recipes_model import IngredientsRecipesModel
from models.ingredients_model import IngredientsModel
from db import db
from logs import Logger


class TestUserModel (unittest.TestCase):

    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()
    email = 'pepe@mail.com'
    password = '1234'

    def setUp(self):
        db.metadata.create_all(self.engine)

    def tearDown(self):
        db.metadata.drop_all(self.engine)

    def test_user_creation(self):
        self.session.add(UserModel(self.email, self.password))
        self.session.commit()
        result = self.session.query(UserModel).all()
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
