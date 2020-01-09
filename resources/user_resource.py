import json
import flask

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity
)
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp

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
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return {'message': 'User found'}, 200

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'User not found'}, 404
        user.delete_user()
        return {'User deleted'}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = _user_parser.parse_args()

        user = UserModel.find_by_email(data['email'])

        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {'message': 'Invalid credentials'}, 401


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200
