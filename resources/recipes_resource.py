from flask_restful import Resource, reqparse

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
        recipe = RecipeModel.find_by_name(name)
        # No devolvemos un objeto json, devolvemos una respuesta Flask porque
        # todavia no sabemos si la logica de negocio (el controlador) ha fallado
        # y con que codigo ha fallado. En los recursos no se realiza tratamiento
        # de errores
        # if not recipe:
        #     raise RecipeNotFoundError

        # return recipe.json()
        return null

    def post(self, name):
        logger = Logger('post::recipe::resources::flask')
        logger.debug('Starting recipe posting')

        # NO ACOPLAMOS EL ENRUTADO CON EL MODELO
        # Todo tratamiento require del controlador que es el encargado de implementar
        # la logica de negocio. Devolvemos siempre un FlaskResponse con un status y un body
        # El contenido del FlaskResponse lo decide el controlador

        # data = Recipe.parser.parse_args()

        # recipe = RecipeModel(name, **data)

        # return recipe.json(), 201

        return null


class RecipesList(Resource):
    def get(self):
        logger = Logger('get::recipeslist::resources::flask')
        logger.debug('Starting recipes list query')
        return {
            'recipes': [
                recipe.json() for recipe in RecipeModel.query.all()
            ]
        }
