from db import db
from logs import Logger


class IngredientsModel(db.Model):
    __tablename__ = 'ingredients'

    name = db.Column(db.String(30), primary_key=True)
    in_recipes = db.relationship(
        'IngredientsRecipesModel',
        backref='ingredient_for_recipe',
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name

    def save(self):
        logger = Logger('save::ingredientsmodel::models::flask')
        logger.debug('Starting save ingredient in database')
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        logger = Logger('findbyname::ingredientsmodel::models::flask')
        logger.debug('Searching ingredient by name')
        return cls.query.filter_by(name=name).first()
