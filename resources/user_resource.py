import json
import flask

from flask_restful import Resource, reqparse

from controllers.user_creation import user_creation
from logs import Logger


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
