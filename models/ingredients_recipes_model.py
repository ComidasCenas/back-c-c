from db import db

from logs import Logger

ingredient_recipe = db.Table(
    'ingredient_of_recipe',
    Base.metadata,
    db.Column('ingredient_recipe_id', db.Integer, primary_key=True),
    db.Column('ingredient_name', db.Integer, db.ForeignKey(
        'ingredientsrecipes.id')),
    db.Column('recipe_id', db.Integer, db.ForeignKey(ingredientsrecipes.id))
)


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

    recipes = db.Relationship(
        'ingredientsrecipes',
        secondary=ingredient_recipe,
        primaryjoin=recipe_id == ingredient_recipe.c.recipe_id
        secondaryjoin=recipe_id == ingredient_recipe.c.ingredient_name
        backref='recipe')

    def __init__(self, quantity, recipe, ingredient):
        self.quantity = quantity
        self.recipe = recipe
        self.ingredient = ingredient

    def save(self):
        logger = Logger('save:ingredientsrecipesmodel::models::flask')
        logger.debug('Starting save relation between ingredient and recipe')
        db.session.add(self)
        db.session.commit()
