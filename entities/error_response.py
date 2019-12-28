import json

from errors.user_errors import user_errors
from errors.recipe_errors import recipe_errors


class ErrorResponse():
    def __init__(self, type_error, domain):
        type_errors_dic = {
            'user': user_errors,
            'recipe': recipe_errors
        }
        self.error = type_errors_dic[domain][type_error]['message']
        self.code = type_errors_dic[domain][type_error]['status']

    def to_json(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
