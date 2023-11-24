from entities.user import User
from database import get_db_connection


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    def __init__(self, connection):

        self._connection = connection

    def find_user(self, username):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM users WHERE username = ?',
            (username)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def find_user_id(self, username):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM users WHERE username = ?',
            (username)
        )

        row = cursor.fetchone()

        return row["user_id"]

    def find_user_by_id(self, user_id):

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM users WHERE user_id = ?',
            (user_id)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create_user(self, user):

        cursor = self._connection.cursor()

        cursor.execute(
            'insert into users(username, password) values(?, ?)',
            (user.username, user.password)
        )

        return user


user_repository = UserRepository(get_db_connection())
