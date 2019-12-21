import json
from errors import errors

class ErrorResponse():
    def __init__(self, typeError):
        self.error = errors[typeError]['message']
        self.code = errors[typeError]['status']

    def toJson(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
