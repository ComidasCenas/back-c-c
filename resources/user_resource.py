import json
import flask

from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from controllers.get_user_by_id import get_user_by_id
from controllers.user_creation import user_creation
from entities.user_entity import User
from logs import Logger
from models.user_model import UserModel

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help='This field cannot be blank'
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help='This field cannot be blank'
                          )


class UserRegister(Resource):
    def post(self):
        logger = Logger('post::userregister::resouces::flask')
        logger.debug('Posting user registration')
        # La auth de la app
        data = _user_parser.parse_args()

        response = user_creation(**data)
        flaskResponse = flask.Response(response.body, status=response.status)
        flaskResponse.headers['Content-Type'] = 'application/json'
        return flaskResponse


class UserFinder(Resource):
    @classmethod
    @jwt_required
    def get(cls, user_id):
        logger = Logger('get::userfinderbyid::resources::flask')
        logger.debug('Getting user by id')

        response = get_user_by_id(user_id)
        flaskResponse = flask.Response(response.body, status=response.status)
        flaskResponse.headers['Content-Type'] = 'application/json'
        return flaskResponse

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'User not found'}, 404
        user.delete_user()
        return {'User deleted'}, 200
