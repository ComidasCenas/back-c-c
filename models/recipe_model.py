from db import db

from logs import Logger


class RecipeModel(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    instructions = db.Column(db.String(300))
    photo = db.Column(db.BLOB)
    recipe_child = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    child_recipes = db.relationship(
        'RecipeModel',
        remote_side=[id],
        backref='related_recipe',
        uselist=False
    )

    ingredients = db.relationship(
        'IngredientsRecipesModel',
        backref='recipe',
        lazy='dynamic'
    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, recipe_entity):
        self.name = recipe_entity.name
        self.instructions = recipe_entity.instructions
        self.user_id = recipe_entity.user_id
        self.photo = recipe_entity.photo

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
