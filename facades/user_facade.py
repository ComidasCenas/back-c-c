# from werkzeug.security import safe_str_cmp


class UserFacade():
    def creation_validation(self, user):
        return self._email_validation(user.email) and self._password_validation(user.password)

    def _email_validation(self, email):
        return True

    def _password_validation(self, password):
        return True


user_facade = UserFacade()
