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
        logger.debug('Searchin user by email')
        return cls.query.filter_by(email=email).first()
