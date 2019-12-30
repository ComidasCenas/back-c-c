from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from os import environ

from security import authenticate, identity
from db import db
from resources.user_resource import UserRegister
from resources.recipes_resource import Recipe, RecipesList
from logs import Logger

logger = Logger('app::flask')
logger.info('Starting app')

app_port = environ['APP_PORT']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DB_PATH']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = environ['APP_SECRET_KEY']
api = Api(app)


@app.before_first_request
def create_tables():
    logger.debug('Creating database')
    db.create_all()


logger.debug('Instantiation JWT')
jwt = JWT(app, authenticate, identity)

logger.debug('Creating routes')
api.add_resource(UserRegister, '/register')
api.add_resource(Recipe, '/recipe/<string:name>')
api.add_resource(RecipesList, '/recipes')


if __name__ == '__main__':
    db.init_app(app)
    # Debug mode should never be used in a production environment!
    app.run(port=app_port, debug=True)
