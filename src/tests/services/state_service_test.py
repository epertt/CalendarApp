import unittest
import datetime
from entities.user import User

from services.state_service import (
    StateService,
    InvalidCredentialsError,
)

from services.user_service import (
    UserService
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


class TestStateService(unittest.TestCase):
    def setUp(self):
        self.fake_user_repo = FakeUserRepository()
        self.state_service = StateService(self.fake_user_repo)
        self.user_service = UserService(self.fake_user_repo)

        self.test_users = []
        self.test_users.append(User("user", "pass", len(self.test_users)))
        self.test_users.append(User("foo", "bar", len(self.test_users)))

        for test_user in self.test_users:
            self.user_service.add_user(
                test_user.username, test_user.password)

    def test_login_logs_in_with_correct_credentials(self):
        self.state_service.login(
            self.test_users[0].username, self.test_users[0].password)
        self.assertEqual(
            self.state_service.get_current_user(), self.test_users[0])

    def test_login_raises_invalidcredentialserror_with_incorrect_password(self):
        with self.assertRaises(InvalidCredentialsError):
            self.state_service.login(
                self.test_users[0].username, "wrongpassword")

    def test_logout(self):
        self.state_service.logout()
        self.assertEqual(self.state_service.get_current_user(), None)

    def test_set_get_current_date(self):
        test_date = datetime.date(2023, 3, 10)
        self.state_service.set_current_date(test_date)
        self.assertEqual(self.state_service.get_current_date(), test_date)
