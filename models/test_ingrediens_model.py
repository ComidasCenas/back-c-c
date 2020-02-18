import unittest
from unittest import TestCase
from unittest.mock import patch
from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.ingredients_model import IngredientsModel
from db import db
from logs import Logger


class TestIngredientModel(TestCase):

    name = 'harina'

    def create_test_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        app.app_context().push()

    def setUp(self):
        self.create_test_app()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_ingredient_creation(self):
        db.session.add(IngredientsModel(self.name))
        db.session.commit()
        result = db.session.query(IngredientsModel).all()
        self.assertEqual(result[0].name, self.name)

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.session.add', autospec=True)
    @patch('db.db.session.commit', autospec=True)
    def test_save_ingredient(self, mocked_commit, mocked_add, mocked_debug):
        test_ingredient = IngredientsModel(self.name)

        test_ingredient.save()

        ingredient_saved = mocked_add.call_args[0][0]

        self.assertEqual(
            mocked_debug.call_args[0][1], 'Starting save ingredient in database')

        self.assertEqual(test_ingredient.name, self.name)

        self.assertEqual(mocked_commit.call_count, 1)

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.Query.filter_by', autospec=True)
    @patch('db.db.Query.first', autospec=True)
    def test_find_ingredient_by_name(self, mocked_first, mocked_filter_by, mocked_debug):
        class mock_query_first():
            def first(self):
                mocked_first.call_count = 1

        mocked_filter_by.return_value = mock_query_first()

        test_ingredient = IngredientsModel(self.name)

        test_ingredient.find_by_name(test_ingredient.name)

        self.assertEqual(
            mocked_debug.call_args[0][1], 'Searching ingredient by name')

        self.assertEqual(mocked_filter_by.call_args[1]['name'], self.name)

        self.assertEqual(mocked_first.call_count, 1)
