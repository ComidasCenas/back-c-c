from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def __repr__(self):
        return f'User: {self.email}'
