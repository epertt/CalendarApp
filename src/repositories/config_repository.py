from entities.config import Config
from database import get_db_connection


def get_config_by_row(row, user):
    if not row:
        config_repository.set_single_user(user, "off")
        return config_repository.get_user_config(user)
    return Config(user.user_id, {"single_user": row["single_user"]})


class ConfigRepository:
    """A class responsible for config-related database actions
    """
    def __init__(self, connection):

        self._connection = connection

    def clear_single_user(self):
        """Sets the single user mode config option to 'off' for all users
        """
        cursor = self._connection.cursor()

        cursor.execute(
            'UPDATE config SET single_user=?',
            ("off",)
        )

        self._connection.commit()

    def set_single_user(self, user, value):
        """Sets the 'single user mode' config option for the specified user

            Args:
                user (User): a User object representing the user whose configuration to change
                value (String): the value to set the 'single user mode' config option to

            Returns: a Config object representing the user's configuration
        """
        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT OR REPLACE INTO config(user_id, single_user) VALUES(?, ?)',
            (user.user_id, value,)
        )

        self._connection.commit()

        return self.get_user_config(user)

    def get_current_single_user_id(self):
        """Returns the user id of the user who currently has 'single user mode' turned on

        Returns:
            Integer: the user_id of the user who currently has 'single user mode' turned on
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT user_id FROM config WHERE single_user=?',
            ("on",)
        )

        row = cursor.fetchone()

        return row["user_id"] if row else None

    def get_user_config(self, user):
        """Returns the configuration of the specified user

        Args:
            user (User): a User object representing the user whose config to look up

        Returns: a Config object representing the specified user's configuration
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM config WHERE user_id=?',
            (user.user_id,)
        )

        row = cursor.fetchone()

        return get_config_by_row(row, user)


config_repository = ConfigRepository(get_db_connection())
