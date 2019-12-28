from db import db

from logs import Logger


class RecipeModel(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    ingredients = db.Column(db.String(100))
    instructions = db.Column(db.String(300))

    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def json(self):
        return {'name': self.name, 'ingredients': self.ingredients, 'instructions': self.instructions}

    @classmethod
    def find_by_name(cls, name):
        logger = Logger('findbyname::recipemodel::models::flask')
        logger.debug('Searching recipe by name')
        return cls.query.filter_by(name=name).first()

    def save(self):
        logger = Logger('save::recipemodel::models::flask')
        logger.debug('Recipe saved in database')
        db.session.add(self)
        db.session.commit()

    def delete(self):
        logger = Logger('delete::usermodel::models::flask')
        logger.debug('Recipe deleted from database')
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_recipes_list(cls):
        logger = Logger('find_all::recipemodel::models::flask')
        logger.debug('Recipes list returned')
        return cls.query.all()
