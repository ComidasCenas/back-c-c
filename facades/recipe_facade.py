class RecipeFacade():
    def recipe_creation_validation(self, recipe):
        return self._name_validation(recipe.name) and self._ingredients_validation(recipe.ingredients) and self._instruction_validation(recipe.instructions)

    def _name_validation(self, name):
        return True

    def _ingredients_validation(self, ingredients):
        return True

    def _instruction_validation(self, instructions):
        return True


recipe_facade = RecipeFacade()
