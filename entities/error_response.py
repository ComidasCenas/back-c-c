import json
from errors.recipe_errors import recipe_errors
from errors.user_errors import user_errors


class ErrorResponse():
    def __init__(self, typeError, domain):
        errors_domain_dic = {
            'user': user_errors,
            'recipe': recipe_errors
        }

        self.error = errors_domain_dic[domain][typeError]['message']
        self.code = errors_domain_dic[domain][typeError]['status']

    def toJson(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
