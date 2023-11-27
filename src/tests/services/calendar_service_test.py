import unittest
from entities.user import User

from services.calendar_service import (
    CalendarService,
    UserExistsError,
    UserDoesNotExistError,
    InvalidCredentialsError,
)


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_user(self, username):
        user = list(
            filter(lambda u: u is not None and u.username == username, self.users))
        return user[0] if len(user) > 0 else None

    def find_user_by_id(self, user_id):
        user = list(
            filter(lambda u: u is not None and u.user_id == user_id, self.users))
        return user[0] if len(user) > 0 else None

    def find_user_id(self, user):
        user = self.find_user(user.username)
        return user.user_id if user is not None else None

    def create_user(self, user):
        user = User(user.username, user.password, len(self.users))
        self.users.append(user)
        return self.find_user(user.username)

    def delete_user(self, user):
        user_index = self.users.index(user)
        self.users = self.users[:user_index]+[None]+self.users[user_index+1:]
        return self.find_user(user.username)


class TestCalendarService(unittest.TestCase):
    def setUp(self):
        self.calendar_service = CalendarService(FakeUserRepository())

        self.test_users = []
        self.test_users.append(User("user", "pass", len(self.test_users)))
        self.test_users.append(User("foo", "bar", len(self.test_users)))

        for test_user in self.test_users:
            self.calendar_service.add_user(
                test_user.username, test_user.password)

    def test_get_user_by_username(self):
        self.assertEqual(
            self.calendar_service.get_user_by_username(
                self.test_users[0].username),
            self.test_users[0]
        )

    def test_get_user_by_username_raises_userdoesnotexisterror_if_user_not_found(self):
        with self.assertRaises(UserDoesNotExistError):
            self.calendar_service.get_user_by_username("userthatdoesnotexist")

    def test_add_user(self):
        created_user = self.calendar_service.add_user(
            "test", "hunter2"
        )

        test_user = User("test", "hunter2", len(self.test_users))

        self.test_users.append(test_user)
        self.assertEqual(
            created_user,
            self.test_users[len(self.test_users)-1]
        )

    def test_delete_user(self):
        self.assertEqual(
            self.calendar_service.remove_user(self.test_users[0]),
            None
        )

    def test_add_user_raises_userexistserror_if_user_exists(self):
        with self.assertRaises(UserExistsError):
            self.calendar_service.add_user(
                self.test_users[1].username, self.test_users[1].password)

    def test_get_user_id(self):
        self.assertEqual(
            self.calendar_service.get_user_id(self.test_users[1]),
            self.test_users[1].user_id
        )

    def test_get_user_id_raises_userdoesnotexisterror_if_user_not_found(self):
        test_user = User("userthatdoesnotexist", "password")
        with self.assertRaises(UserDoesNotExistError):
            self.calendar_service.get_user_id(test_user)

    def test_get_user_by_id(self):
        self.assertEqual(
            self.calendar_service.get_user_by_id(1),
            self.test_users[1]
        )
