from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from errors.user_errors import user_errors
from os import environ

from security import authenticate, identity
from db import db
from resources.user_resource import UserRegister, User
from resources.recipes_resource import Recipe, RecipesList
from flask_migrate import Migrate
from logs import Logger

logger = Logger('app::flask')
logger.info('Starting app')

app_port = environ['APP_PORT']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DB_PATH']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = environ['APP_SECRET_KEY']

migrate = Migrate(app, db)
api = Api(app)


logger.debug('Instantiation JWT')
jwt = JWT(app, authenticate, identity)

logger.debug('Creating routes')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Recipe, '/recipe/<string:name>')
api.add_resource(RecipesList, '/recipes')

db.init_app(app)

if __name__ == '__main__':
    # Debug mode should never be used in a production environment!
    app.run(port=app_port, debug=True)
