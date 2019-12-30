import flask

from flask_restful import Resource, reqparse

from controllers.recipe_list_reading import recipe_list_reading
from controllers.recipe_reading import recipe_reading
from controllers.recipe_creation import recipe_creation
from models.recipe_model import RecipeModel
from logs import Logger


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

    def get(self, name):
        logger = Logger('get::recipe::resouces::flask')
        logger.debug('Starting recipe query')
        response = recipe_reading(name)
        return response

    def post(self, name):
        logger = Logger('post::recipe::resources::flask')
        logger.debug('Starting recipe posting')

        data = Recipe.parser.parse_args()

        response = recipe_creation(name, **data)
        flaskResponse = flask.Response(response.body, status=response.status)
        flaskResponse.headers['Content-Type'] = 'application/json'
        return flaskResponse


class RecipesList(Resource):
    def get(self):
        logger = Logger('get::recipeslist::resources::flask')
        logger.debug('Starting recipes list query')
        recipe_list_reading()
