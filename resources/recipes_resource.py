import flask

from flask_restful import Resource, reqparse

from controllers.recipes_creation import recipes_creation
from helpers.http_response_decorator import http_response
from logs import Logger
from models.recipe_model import RecipeModel


class Recipe(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ingredients',
                        type=str,
                        required=True,
                        help='This field cannot be empty'
                        )
    parser.add_argument('instructions',
                        type=str,
                        required=True,
                        help='This field cannot be empty'
                        )

    @http_response
    def get(self, name):
        logger = Logger('get::recipe::resouces::flask')
        logger.debug('Starting recipe query')
        # ecipe = RecipeModel.find_by_name(name)
        # No devolvemos un objeto json, devolvemos una respuesta Flask porque
        # todavia no sabemos si la logica de negocio (el controlador) ha
        # fallado
        # y con que codigo ha fallado. En los recursos no se realiza
        # tratamiento
        # de errores
        # if not recipe:
        #     raise RecipeNotFoundError

        # return recipe.json()
        return None


class RecipesList(Resource):

    def get(self):
        logger = Logger('get::recipeslist::resources::flask')
        logger.debug('Starting recipes list query')
        return {
            'recipes': [
                recipe.json() for recipe in RecipeModel.query.all()
            ]
        }

    def post(self):
        logger = Logger('post::recipe::resources::flask')
        logger.debug('Starting recipe posting')

        data = flask.request.json
        response = recipes_creation(data)
        flaskResponse = flask.Response(response.body, status=response.status)
        flaskResponse.headers['Content-Type'] = 'application/json'
        return flaskResponse
