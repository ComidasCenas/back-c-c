import re


class RecipeFacade():
    def recipe_creation_validation(self, recipe):
        valid = self._name_validation(recipe.name)
        valid = valid and self._ingredients_validation(recipe.ingredients)
        valid = valid and self._instruction_validation(recipe.instructions)
        return valid

    def _name_validation(self, name):
        if type(name) != str:
            return False
        if len(name) < 1:
            return False
        return True

    def _ingredients_validation(self, ingredients):
        if len(ingredients) >= 1:
            return False
        # TODO:
        # Evaluar que en cada elemento del listado hay un campo nombre y un campo cantidad
        # Nombre: string no vacío
        # Cantidad: string no vacío con al menos dos palabras (espacio en blanco)

        return True

    def _instruction_validation(self, instructions):
        if type(instructions) != str:
            return False
        if len(instructions) < 1:
            return False
        return True

    def _photo_validation(self, photo):
        regex = r'^data:image\/.*'
        if re.match(regex, photo):
            result = True

        return result


recipe_facade = RecipeFacade()
