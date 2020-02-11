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

    name = 'Bizcocho'
    instructions = 'Se te ha quemado'
    user_id = 1
    photo = 'foto del bizcocho quemado'

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

    def test_recipe_creation(self):
        db.session.add(RecipeModel())
        db.session.commit()  # Por qué este commit no se mockea?
        result = db.session.query(RecipeModel).all()
        self.assertEqual(result[0].name, self.name)
        self.assertEqual(result[0].instructions, self.instructions)
        self.assertEqual(result[0].user_id, self.user_id)
        self.assertEqual(result[0].photo, self.photo)
