from db import db

from logs import Logger


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))
    recipes = db.relationship(
        'RecipeModel',
        backref='author',
        lazy='dynamic'
    )

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save(self):
        logger = Logger('save::usermodel::models::flask')
        logger.debug('Starting save user in database')
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        logger = Logger('findbyemail::usermodel::models::flask')
        logger.debug('Searching user by email')
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, user_id):
        logger = Logger('findbyid::usermodel::models::flask')
        logger.debug('Searching user by id')
        return cls.query.filter_by(id=user_id).first()

    def delete_user(self):
        logger = Logger('deleteuser::usermodel::models::flask')
        logger.debug('Deleting item')
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User: {self.email}'
