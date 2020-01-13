import json


class User():
    def __init__(self, email, user_id=None, password=None):
        self.user_id = user_id
        self.email = email
        self.password = password

    def to_json(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
