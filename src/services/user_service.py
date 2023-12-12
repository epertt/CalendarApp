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
        """Looks up a user matching the input username

        Args:
            username (String): the username of the user to look up

        Returns:
            User: a User object with a matching username
        """
        user = self._user_repository.find_user(username)
        return user

    def get_user_id(self, user):
        """Looks up a user id matching the input user

        Args:
            user (User): a User object to look up the id of

        Returns:
            Integer: the user id matching the user
        """
        user_id = self._user_repository.find_user_id(user)
        return user_id

    def get_user_by_id(self, user_id):
        """Looks up a user matching the input user id

        Args:
            user_id (Integer): the user id to look up the matching User object for

        Returns:
            User: a User object matching the user id
        """
        user = self._user_repository.find_user_by_id(user_id)
        return user

    def add_user(self, username, password):
        """Adds a new user to the database

        Args:
            username (String): the new user's username
            password (String): the new user's password

        Raises:
            UserExistsError: if a user with the specified username already exists,
            an error is raised

        Returns:
            User: a User object representing the newly added user
        """
        if self.get_user_by_username(username):
            raise UserExistsError()
        user = User(username, password)
        return self._user_repository.create_user(user)

    def remove_user(self, user):
        """Removes an existing user from the database

        Args:
            user (User): a User object representing the User to be removed

        Raises:
            UserDoesNotExistError: if a User matching the input User is not found,
            an error is raised

        Returns:
            User: a User object representing the deleted user
        """
        if not self.get_user_by_username(user.username):
            raise UserDoesNotExistError()
        return self._user_repository.delete_user(user)


user_service = UserService()
