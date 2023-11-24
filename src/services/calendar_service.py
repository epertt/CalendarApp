from entities.user import User

from repositories.user_repository import user_repository as default_user_repository
from repositories.note_repository import note_repository as default_note_repository


class UserExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class CalendarService:
    def __init__(self, user_repository=default_user_repository, note_repository=default_note_repository):
        self._user = None
        self._user_repository = user_repository
        self._note_repository = note_repository

    def get_logged_in_user(self):
        return self._user

    def get_user(self, username):
        return self._user_repository.find_user(username)
    
    def get_user_id(self, username):
        return self._user_repository.find_user_id(username)

    def get_notes(self, date=None):
        user_id = self.get_user_id(self._user.username)
        if date:
            return self._note_repository.get_notes(user_id, date.timestamp())
        return self._note_repository.get_notes(user_id)

    def create_user(self, username, password):
        if self.get_user(username):
            raise UserExistsError("username already exists")
        user = User(username, password)
        return self._user_repository.create_user(user)

    def login(self, username, password):
        user = self._user_repository.find_user(username)

        if not user or user.password != password:
            raise InvalidCredentialsError()

        self._user = user

        return user

    def logout(self):
        self._user = None


calendar_service = CalendarService()
