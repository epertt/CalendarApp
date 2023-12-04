from repositories.user_repository import user_repository as default_user_repository


class InvalidCredentialsError(Exception):
    "Username or password are incorrect"


class StateService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository
        self._user = None
        self._date = None

    def set_current_user(self, user):
        self._user = user

    def get_current_user(self):
        return self._user

    def set_current_date(self, date):
        self._date = date

    def get_current_date(self):
        return self._date

    def login(self, username, password):
        user = self._user_repository.find_user(username)

        if not user or user.password != password:
            raise InvalidCredentialsError()

        self.set_current_user(user)

        return user

    def logout(self):
        self._user = None


state_service = StateService()
