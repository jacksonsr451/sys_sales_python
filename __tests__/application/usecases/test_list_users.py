from unittest import TestCase

from src.applications.usecases.list_users.list_users import ListUsers
from src.applications.usecases.list_users.list_users_gateway import ListUsersGateway
from src.applications.usecases.list_users.list_users_presenter_interface import ListUsersPresenterInterface


class TestListUsers(TestCase):
    def setUp(self) -> None:
        self.repository: ListUsersGateway = ListUsersRepository()
        self.list_users = ListUsers(repository=self.repository)
        self.presenter: ListUsersPresenterInterface = ListUsersPresenter()

    def test_if_list_users_is_instance_of(self):
        self.assertIsInstance(self.list_users, ListUsers)

    def test_if_list_users_return_a_list(self):
        self.list_users.list(presenter=self.presenter)
        self.assertIsInstance(self.presenter.get_view_model(), list)

    def tearDown(self) -> None:
        self.repository = None
        self.list_users = None
        self.presenter = None


class ListUsersRepository(ListUsersGateway):
    def list_users(self) -> list:
        return []


class ListUsersPresenter(ListUsersPresenterInterface):
    def __init__(self):
        self.users: list = list()

    def present(self, list_users: list):
        self.users = list_users

    def get_view_model(self):
        return self.users
