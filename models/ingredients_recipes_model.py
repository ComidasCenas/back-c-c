from db import db

from logs import Logger


class IngredientsRecipesModel(db.Model):
    __tablename__ = 'ingredientsrecipes'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey('recipes.id')
    )
    ingredient_name = db.Column(
        db.String(30),
        db.ForeignKey('ingredients.id')
    )

    def __init__(self, quantity, recipe, ingredient):
        self.quantity = quantity
        self.recipe = recipe
        self.ingredient = ingredient

    def save(self):
        logger = Logger('save:ingredientsrecipesmodel::models::flask')
        logger.debug('Starting save relation between ingredient and recipe')
        db.session.add(self)
        db.session.commit()
