from flask import Flask
from flask_restful import Resource, Api

from db import db
from resources.user_resource import UserRegister


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, '/users')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000)
