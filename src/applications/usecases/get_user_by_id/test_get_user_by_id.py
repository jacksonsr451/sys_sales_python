from unittest import TestCase

from src.applications.usecases.get_user_by_id.get_user_by_id import GetUserByID
from src.applications.usecases.get_user_by_id.get_user_by_id_gateway import GetUserByIDGateway
from src.applications.usecases.get_user_by_id.get_user_by_id_presenter_interface import GetUserByIDPresenterInterface


class TestGetUserByID(TestCase):
    def setUp(self) -> None:
        self.repository: GetUserByIDGateway = GetUserByIDRepository()
        self.get_user_by_id = GetUserByID(repository=self.repository)
        self.presenter: GetUserByIDPresenterInterface = GetUserByIDPresenter()

    def test_if_get_user_by_id_is_instance_of(self):
        self.assertIsInstance(self.get_user_by_id, GetUserByID)

    def test_if_get_user_by_id_return_a_object(self):
        self.get_user_by_id.get_user(id="123456", presenter=self.presenter)
        self.assertIsInstance(self.presenter.get_view_model(), object)


class GetUserByIDRepository(GetUserByIDGateway):
    def get_user_by_id(self, id: str):
        return object()


class GetUserByIDPresenter(GetUserByIDPresenterInterface):
    def __init__(self):
        self.user = None

    def present(self, user):
        self.user = user

    def get_view_model(self):
        return self.user
