from entities.user import User

from repositories.user_repository import user_repository as default_user_repository
from repositories.note_repository import note_repository as default_note_repository


class UserExistsError(Exception):
    "User already exists"


class UserDoesNotExistError(Exception):
    "User does not exist"


class InvalidCredentialsError(Exception):
    "Username or password are incorrect"


class CalendarService:
    def __init__(self,
                 user_repository=default_user_repository,
                 note_repository=default_note_repository
                 ):
        self._user = None
        self._user_id = None
        self._user_repository = user_repository
        self._note_repository = note_repository

    def get_current_user(self):
        return self._user

    def get_user_by_username(self, username):
        user = self._user_repository.find_user(username)
        return user

    def get_user_id(self, user):
        user_id = self._user_repository.find_user_id(user)
        return user_id

    def get_user_by_id(self, user_id):
        user = self._user_repository.find_user_by_id(user_id)
        return user

    def get_notes_by_date(self, date=None):
        return self._note_repository.get_notes_by_date(self._user_id, date.timestamp())

    def get_notes_all(self):
        return self._note_repository.get_notes_all(self._user_id)

    def add_note(self, date, content):
        return self._note_repository.create_note(self._user_id, date.timestamp(), content)

    def remove_note(self, note):
        return self._note_repository.delete_note(note.note_id)

    def add_user(self, username, password):
        if self.get_user_by_username(username):
            raise UserExistsError()
        user = User(username, password)
        return self._user_repository.create_user(user)

    def remove_user(self, user):
        if not self.get_user_by_username(user.username):
            raise UserDoesNotExistError()
        return self._user_repository.delete_user(user)

    def login(self, username, password):
        user = self._user_repository.find_user(username)

        if not user or user.password != password:
            raise InvalidCredentialsError()

        self._user = user
        self._user_id = self.get_user_id(self._user)

        return user

    def logout(self):
        self._user = None
        self._user_id = None


calendar_service = CalendarService()
