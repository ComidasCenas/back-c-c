from db import db

from logs import Logger


class RecipeRelatedModel(db.Model):
    __tablename__ = 'reciperelated'

    id = db.Column(db.Integer, primary_key=True)
    parent_recipe = db.Column(
        db.Integer,
        db.ForeignKey('recipes.id')
    )
    child_recipe = db.Column(
        db.Integer,
        db.ForeignKey('recipes.id')
    )

    def __init__(self, parent_recipe, child_recipe):
        self.parent_recipe = parent_recipe
        self.child_recipe = child_recipe
