import unittest
from entities.user import User

from services.calendar_service import (
    CalendarService,
    InvalidCredentialsError,
    UserExistsError,
)


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_user(self, username):
        user = filter(lambda user: user.username == username, self.users)
        return list(user)

    def create_user(self, user):
        self.users.append(user)
        return user


class TestCalendarService(unittest.TestCase):
    def setUp(self):
        self.calendar_service = CalendarService(FakeUserRepository())

        self.test_user = User("user", "pass")
        self.new_user = User("foo", "bar")

    def test_create_user(self):
        created_user = self.calendar_service.create_user(
            self.new_user.username, self.new_user.password
        )
        self.assertEqual(self.new_user, created_user)

    def test_create_user_raises_UserExistsError_if_user_exists(self):
        self.calendar_service.create_user(
            self.test_user.username, self.test_user.password
        )
        with self.assertRaises(UserExistsError) as context:
            created_user = self.calendar_service.create_user(
                self.test_user.username, self.test_user.password
            )
        self.assertTrue("username already exists" in str(context.exception))
