class RecipeFacade():
    def recipe_creation_validation(self, recipe):
        return self._name_validation(recipe.name) and self._ingredients_validation(recipe.ingredients) and self._instruction_validation(recipe.instructions)

    def _name_validation(self, name):
        if name:
            return True

    def _ingredients_validation(self, ingredients):
        if len(ingredients) >= 1:
            return True

    # ¿Habría que chequear si los ingredientes son instancias de la entidad ingredientes?

    def _instruction_validation(self, instructions):
        if instructions:
            return True

    def _photo_validation(self, photo):
        if photo:
            return True


recipe_facade = RecipeFacade()
