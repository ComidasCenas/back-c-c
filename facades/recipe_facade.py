class RecipeFacade():
    def recipe_creation_validation(self, recipe):
        valid = self._name_validation(recipe.name)
        valid = valid and self._ingredients_validation(recipe.ingredients)
        valid = valid and self._instruction_validation(recipe.instructions)
        return valid

    def _name_validation(self, name):
        if name:
            return True

    def _ingredients_validation(self, ingredients):
        if len(ingredients) >= 1:
            return True

    def _instruction_validation(self, instructions):
        if instructions:
            return True

    def _photo_validation(self, photo):
        if photo:
            return True


recipe_facade = RecipeFacade()
