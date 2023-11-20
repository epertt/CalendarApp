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
            'select * from users where username = ?',
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

user_repository = UserRepository(get_db_connection())