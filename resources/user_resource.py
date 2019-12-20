from flask_restful import Resource, reqparse

from models.user_model import UserModel
from errors import UserAlreadyExistsError


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
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_email(data.get('email')):
            raise UserAlreadyExistsError

        user = UserModel(**data)
        user.save()

        return {"message": "User created successfully."}, 201
