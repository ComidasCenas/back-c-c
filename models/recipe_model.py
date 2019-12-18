from db import db


class RecipeModel(db.Model):
    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    photo = db.Column(db.LargeBinary)
    instructions = db.Column(db.String(300))

    def __init__(self, name):
        self.name = name
        self.photo = photo
        self.instructions = instructions
