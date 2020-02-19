import unittest
from unittest import TestCase
from unittest.mock import patch
from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import db
from logs import Logger
from models.ingredients_recipes_model import IngredientsRecipesModel


class TestIngredientsRecipesModels(TestCase):
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

    def test_ingredient_tecipe_creation(self):
        pass

    def test_ingredient_tecipe_save(self):
        pass
