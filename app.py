from os import environ

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Resource, Api


from db import db
from errors.user_errors import user_errors
from logs import Logger
from resources.recipes_resource import Recipe, RecipesList
from resources.user_resource import UserRegister, UserFinder, UserLogin, TokenRefresh


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

jwt = JWTManager(app)

logger.debug('Creating routes')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')  # previous /auth
api.add_resource(UserFinder, '/user/<int:user_id>')
api.add_resource(Recipe, '/recipe/<string:name>')
api.add_resource(RecipesList, '/recipes')
api.add_resource(TokenRefresh, '/refresh')

db.init_app(app)

if __name__ == '__main__':
    # Debug mode should never be used in a production environment!
    app.run(port=app_port, debug=True)
