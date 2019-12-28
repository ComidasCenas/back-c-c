import flask

from flask_restful import Resource, reqparse


class AppAuth(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'hash',
        type=str,
        required=True,
        help='This field cannot be blank'
    )

    def post()
