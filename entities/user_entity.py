from helpers.serializable_decorator import serializable


@serializable
class User():
    def __init__(self, email, user_id=None, password=None):
        self.user_id = user_id
        self.email = email
        self.password = password
