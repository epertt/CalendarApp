from entities.user import User

from repositories.user_repository import user_repository as default_user_repository


class UserExistsError(Exception):
    "User already exists"


class UserDoesNotExistError(Exception):
    "User does not exist"


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def get_user_by_username(self, username):
        user = self._user_repository.find_user(username)
        return user

    def get_user_id(self, user):
        user_id = self._user_repository.find_user_id(user)
        return user_id

    def get_user_by_id(self, user_id):
        user = self._user_repository.find_user_by_id(user_id)
        return user

    def add_user(self, username, password):
        if self.get_user_by_username(username):
            raise UserExistsError()
        user = User(username, password)
        return self._user_repository.create_user(user)

    def remove_user(self, user):
        if not self.get_user_by_username(user.username):
            raise UserDoesNotExistError()
        return self._user_repository.delete_user(user)


user_service = UserService()
