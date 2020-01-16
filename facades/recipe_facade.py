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
        regex = r'(\w+\s\w+)'
        for ingredient in ingredients:
            if ingredient.get('name') == None or ingredient.get('quantity') == None:
                return False
            if type(ingredient['name']) != str or len(ingredient['name']) < 1:
                return False
            if type(ingredient['quantity']) != str or len(ingredient['quantity']) < 1:
                return False
            if not re.match(regex, item['quantity']):
                return False

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
