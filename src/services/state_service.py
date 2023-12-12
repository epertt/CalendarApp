from repositories.user_repository import user_repository as default_user_repository
from services.config_service import config_service


class InvalidCredentialsError(Exception):
    "Username or password are incorrect"


class StateService:
    """A service responsible for holding state data about the user currently using the program,
    shared between multiple other views and services
    """

    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository
        self._config_service = config_service
        self._user = None
        self._date = None
        self._single_user = self._config_service.get_current_single_user_id()

    def set_current_user(self, user):
        """Sets the currently logged in user

        Args:
            user (User): a User object representing the currently logged in user
        """
        self._user = user

    def get_current_user(self):
        """Returns the currently logged in user

        Returns:
            User: a User object representing the currently logged in user
        """
        return self._user

    def set_current_date(self, date):
        """Sets the current date shared between the various views

        Args:
            date (Date): a Date object representing a date that's currently shown in the view
        """
        self._date = date

    def get_current_date(self):
        """Returns the current date shared between the various views

        Returns:
            date (Date): a Date object representing a date that's currently shown in the view
        """
        return self._date

    def get_single_user(self):
        """Returns the user id of the user that currently has 'single user mode' enabled, if any

        Returns:
            Integer: the user id of the user that has 'single user mode' enabled, or None if
            no user has turned on the setting
        """
        return self._single_user

    def login(self, username, password):
        """Logs in the user

        Args:
            username (String): the username of the User to log in as
            password (String): the password of the User to log in as

        Raises:
            InvalidCredentialsError: if the user supplies a password that 
            doesn't match the username, an error is raised

        Returns:
            User: a User object representing the user that has successfully logged in
        """
        user = self._user_repository.find_user(username)

        if not user or user.password != password:
            raise InvalidCredentialsError()

        self.set_current_user(user)

        return self.get_current_user()

    def logout(self):
        """Logs out the user and turns off 'single user mode'
        """
        if self._user:
            self._config_service.set_single_user(self._user, "off")
            self._single_user = None
        self._user = None


state_service = StateService()
