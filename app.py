from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from errors import errors

from security import authenticate, identity
from db import db
from resources.user_resource import UserRegister
from resources.recipes_resource import Recipe, RecipesList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'marramiau'
api = Api(app, errors=errors)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(Recipe, '/recipe/<string:name>')
api.add_resource(RecipesList, '/recipes')


if __name__ == '__main__':
    db.init_app(app)
    # Debug mode should never be used in a production environment!
    app.run(port=5000, debug=True)
