from entities.config import Config
from database import get_db_connection


def get_config_by_row(row, user):
    if not row:
        config_repository.set_single_user(user, "off")
        return config_repository.get_user_config(user)
    return Config(user.user_id, {"single_user": row["single_user"]})


class ConfigRepository:
    def __init__(self, connection):

        self._connection = connection

    def clear_single_user(self):
        cursor = self._connection.cursor()

        cursor.execute(
            'UPDATE config SET single_user=?',
            ("off",)
        )

        self._connection.commit()

    def set_single_user(self, user, value):

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT OR REPLACE INTO config(user_id, single_user) VALUES(?, ?)',
            (user.user_id, value,)
        )

        self._connection.commit()

        return self.get_user_config(user)

    def get_current_single_user_id(self):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT user_id FROM config WHERE single_user=?',
            ("on",)
        )

        row = cursor.fetchone()

        return row["user_id"] if row else None

    def get_user_config(self, user):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM config WHERE user_id=?',
            (user.user_id,)
        )

        row = cursor.fetchone()

        return get_config_by_row(row, user)


config_repository = ConfigRepository(get_db_connection())
