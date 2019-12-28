from flask_restful import Resource, reqparse

from models.recipe_model import RecipeModel
from errors.recipe_errors import recipe_errors
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
        recipe = RecipeModel.find_by_name(name)
        if not recipe:
            raise RecipeNotFoundError

        return recipe.json()

    def post(self, name):
        logger = Logger('post::recipe::resources::flask')
        logger.debug('Starting recipe posting')
        # if RecipeModel.find_by_name(name):
        #     raise RecipeAlreadyExistsError

        data = Recipe.parser.parse_args()

        recipe = RecipeModel(name, **data)

        try:
            recipe.save()
        except:
            raise CreatingRecipeError

        return recipe.json(), 201


class RecipesList(Resource):
    def get(self):
        logger = Logger('get::recipeslist::resources::flask')
        logger.debug('Starting recipes list query')
        return {'recipes': [recipe.json() for recipe in RecipeModel.query.all()]}
