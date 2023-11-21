from entities.user import User

from repositories.user_repository import user_repository as default_user_repository


class InvalidCredentialsError(Exception):
    pass


class CalendarService:
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def get_date():
        pass

    def get_user(self, username):
        return self._user_repository.find_user(username)

    def create_user(self, username, password):
        return self._user_repository.create_user(username, password)

    def login(self, username, password):
        user = self._user_repository.find_user(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def logout(self):
        self._user = None


calendar_service = CalendarService()
