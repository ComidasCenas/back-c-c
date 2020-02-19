from flask import Flask
import unittest
from unittest import TestCase
from unittest.mock import patch

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import db
from entities.recipe_entity import Recipe
from logs import Logger
from models.recipe_model import RecipeModel
from models.ingredients_recipes_model import IngredientsRecipesModel
from models.user_model import UserModel


class TestRecipeModel(TestCase):

    recipe_post = {
        'name': 'bizcocho',
        'relatedRecipes': [],
        'ingredients': [
            {
                'name': 'harina',
                'quantity': '200 gr'
            },
            {
                'name': 'huevos',
                'quantity': '3'
            },
            {
                'name': 'azucar',
                'quantity': '90 gr'
            },
        ],
        'recipeSteps': 'mezcla los ingrdientes y al horno',
        'photo': b'se ha quemado mucho'
    }

    email = 'pepe@mail.com'
    password = '1234'

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

        db.session.add(UserModel(self.email, self.password))
        db.session.commit()
        user_test = db.session.query(UserModel).first()

        recipe_test = Recipe(self.recipe_post, user_test.id)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_recipe_creation(self):
        db.session.add(UserModel(self.email, self.password))
        db.session.commit()
        user_test = db.session.query(UserModel).first()

        recipe_test = Recipe(self.recipe_post, user_test.id)

        db.session.add(RecipeModel(recipe_test))
        db.session.commit()

        result = db.session.query(RecipeModel).all()

        self.assertEqual(result[0].name, self.recipe_post.get('name'))
        self.assertEqual(result[0].instructions,
                         self.recipe_post.get('recipeSteps'))
        self.assertEqual(result[0].user_id, user_test.id)
        self.assertEqual(result[0].photo, self.recipe_post.get('photo'))

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.session.add', autospec=True)
    @patch('db.db.session.commit', autospec=True)
    def test_recipe_save(self, mocked_commit, mocked_add, mocked_debug):
        db.session.add(UserModel(self.email, self.password))
        db.session.commit()
        user_test = db.session.query(UserModel).first()

        recipe_test = Recipe(self.recipe_post, user_test.id)

        recipe_model = RecipeModel(recipe_test)

        recipe_model.save()

        self.assertEqual(
            mocked_debug.call_args[0][1], 'Recipe saved in database')

        recipe_saved = mocked_add.call_args[0][0]

        self.assertEqual(recipe_saved.name, self.recipe_post.get('name'))
        self.assertEqual(recipe_saved.instructions,
                         self.recipe_post.get('recipeSteps'))
        self.assertEqual(recipe_saved.user_id, user_test.id)
        self.assertEqual(recipe_saved.photo, self.recipe_post.get('photo'))

        self.assertEqual(
            mocked_commit.call_count,
            2
        )

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.Query.filter_by', autospec=True)
    @patch('db.db.Query.first', autospec=True)
    def test_find_recipe_by_name(self, mocked_first, mocked_filter, mocked_debug):
        db.session.add(UserModel(self.email, self.password))
        db.session.commit()
        user_test = db.session.query(UserModel).first()

        recipe_test = Recipe(self.recipe_post, user_test.id)

        recipe_model = RecipeModel(recipe_test)

        recipe_model.find_by_name(recipe_model.name)

        self.assertEqual(
            mocked_debug.call_args[0][1], 'Searchin recipe by name')

        self.assertEqual(
            mocked_filter.call_args[1]['name'], self.recipe_post.get('name'))
        # print('-----------------------------------------')
        # print('mocked_filter.call_args[1]', mocked_filter.call_args[1])
        # print('-----------------------------------------')

        self.assertEqual(mocked_first.call_count, 1)

    @patch('logs.Logger.__init__', lambda x, y: None)
    @patch('logs.Logger.debug', autospec=True)
    @patch('db.db.session.delete', autospec=True)
    @patch('db.db.session.commit', autospec=True)
    def test_delete_recipe(self, mocked_commit, mocked_deletion, mocked_debug):
        db.session.add(UserModel(self.email, self.password))
        db.session.commit()
        user_test = db.session.query(UserModel).first()

        recipe_test = Recipe(self.recipe_post, user_test.id)

        recipe_model = RecipeModel(recipe_test)

        recipe_model.delete()

        self.assertEqual(
            mocked_debug.call_args[0][1], 'Recipe deleted from database')

        self.assertEqual(mocked_commit.call_count, 2)

        recipe_deleted = mocked_deletion.call_args[0][0]

        self.assertEqual(recipe_deleted, recipe_model)
