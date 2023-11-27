from entities.user import User

from repositories.user_repository import user_repository as default_user_repository
from repositories.note_repository import note_repository as default_note_repository


class UserExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class CalendarService:
    def __init__(self,
                 user_repository=default_user_repository,
                 note_repository=default_note_repository
                 ):
        self._user = None
        self._user_id = None
        self._user_repository = user_repository
        self._note_repository = note_repository

    def get_user(self, username):
        return self._user_repository.find_user(username)

    def get_user_id(self, username):
        return self._user_repository.find_user_id(username)

    def get_notes_by_date(self, date=None):
        return self._note_repository.get_notes_by_date(self._user_id, date.timestamp())

    def get_notes_all(self):
        return self._note_repository.get_notes_all(self._user_id)

    def add_note(self, date, content):
        return self._note_repository.create_note(self._user_id, date.timestamp(), content)

    def delete_note(self, note):
        return self._note_repository.delete_note(note.note_id)

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
        self._user_id = self.get_user_id(self._user.username)

        return user

    def logout(self):
        self._user = None
        self._user_id = None


calendar_service = CalendarService()
