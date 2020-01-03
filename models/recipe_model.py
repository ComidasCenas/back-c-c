from db import db

from logs import Logger


class RecipeModel(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    instructions = db.Column(db.String(300))
    photo = db.Column(db.BLOB)
    child_recipes = db.relationship(
        'RecipeRelatedModel',
        backref='parents',
        lazy='dynamic'
    )
    parent_recipes = db.relationship(
        'RecipeRelatedModel',
        backref='children',
        lazy='dynamic'
    )
    ingredients = db.relationship(
        'IngredientsRecipesModel',
        backref='recipe',
        lazy='dynamic'
    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, instructions, user_id, photo, recipes_related=[]):
        self.name = name
        self.instructions = instructions
        self.user_id = user_id
        self.photo = photo
        self.recipes_related = []

    @classmethod
    def find_by_name(cls, name):
        logger = Logger('findbyname::recipemodel::models::flask')
        logger.debug('Searchin recipe by name')
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
