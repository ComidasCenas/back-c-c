from errors.user_errors import user_errors
from errors.recipe_errors import recipe_errors
from helpers.serializable_decorator import serializable


@serializable
class ErrorResponse():
    def __init__(self, type_error, domain):
        type_errors_dic = {
            'user': user_errors,
            'recipe': recipe_errors
        }
        self.error = type_errors_dic[domain][type_error]['message']
        self.code = type_errors_dic[domain][type_error]['status']
