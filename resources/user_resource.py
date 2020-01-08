import json
import flask

from flask_restful import Resource, reqparse

from controllers.user_creation import user_creation
from entities.user_entity import User
from logs import Logger
from models.user_model import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='This field cannot be blank'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be blank'
                        )

    def post(self):
        logger = Logger('post::userregister::resouces::flask')
        logger.debug('Posting user registration')
        # La auth de la app
        data = UserRegister.parser.parse_args()

        response = user_creation(**data)
        flaskResponse = flask.Response(response.body, status=response.status)
        flaskResponse.headers['Content-Type'] = 'application/json'
        return flaskResponse


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'User not found'}, 404
        return {
            'id': user.id,
            'email': user.email
        }

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'User not found'}, 404
        user.delete_user()
        return {'User deleted'}
