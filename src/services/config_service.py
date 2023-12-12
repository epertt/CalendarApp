from repositories.config_repository import config_repository as default_config_repository


class ConfigService:
    """A service responsible for handling configuration related actions
    """
    def __init__(self, config_repository=default_config_repository):
        self._config_repository = config_repository

    def set_single_user(self, user, value):
        """Sets the single user config option for a user

        Args:
            user (User): a User object representing the user to set the config option for
            value (String): either 'on' or 'off' to toggle the setting

        Returns:
            Config: a Config object representing the configuration of the user
        """
        return self._config_repository.set_single_user(user, value)

    def get_current_single_user_id(self):
        """Returns the user id for the user that currently has the 'single user mode' 
        config option enabled

        Returns:
            Integer: the user id of the user that currently has the 'single user mode' 
            config option enabled
        """
        return self._config_repository.get_current_single_user_id()

    def clear_single_user(self):
        """Sets the 'single user mode' config option to 'off' for all users
        """
        self._config_repository.clear_single_user()

    def get_user_config(self, user):
        """Returns the config values of the input user

        Args:
            user (User): a User object representing the user to retrieve
            the config values for

        Returns:
            Config: a Config object representing the configuration of the input user
        """
        return self._config_repository.get_user_config(user)


config_service = ConfigService()
