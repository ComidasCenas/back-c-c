class User():
    def __init__(self, email, password, user_id=None):
        self.user_id = user_id
        self.email = email
        self.password = password

    def to_json(self):
        return {
            'user_id': self.user_id,
            'email': self.email
        }
