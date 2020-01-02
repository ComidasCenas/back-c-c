class Recipe():
    def __init__(self, name, ingredients, instructions, photo, recipes_related=None):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.photo = photo

        self.recipes_related = list() if (recipes_related is None) else recipes_related
