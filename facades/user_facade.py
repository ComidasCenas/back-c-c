class UserFacade():
    def creation_validation(self, user):
        validation = self._email_validation(user.email)
        validation = validation and self._password_validation(user.password)
        return validation

    def _email_validation(self, email):
        return True

    def _password_validation(self, password):
        return True


user_facade = UserFacade()
