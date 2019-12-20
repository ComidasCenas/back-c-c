from flask_restful import Resource, reqparse

from models.recipe_model import RecipeModel
from errors import RecipeNotFoundError, RecipeAlreadyExistsError, CreatingRecipeError


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
        recipe = RecipeModel.find_by_name(name)
        if not recipe:
            raise RecipeNotFoundError

        return recipe.json()

    def post(self, name):
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
        return {'recipes': [recipe.json() for recipe in RecipeModel.query.all()]}
