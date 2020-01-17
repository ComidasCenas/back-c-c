import unittest
from unittest.mock import MagicMock

from .. recipes_creation import RecipeCreation

# db library simplemente graba el diccionario que le pases usando sql

class TestRecipeCreation(unittest.TestCase):
    def test_given_a_recipe_save_it(self):
        recipe = {'name':'a name', 'ingredients':{'name':'an ingredient', 'quantity': '1'}}
        db_library = MagicMock()
        recipe_to_save = RecipeCreation(db_library)

        recipe_to_save.create_recipe(recipe)

        db_library.save.assert_called()
        
