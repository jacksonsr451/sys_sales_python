from unittest import TestCase

from src.applications.usecases.delete_user_by_id.delete_user_by_id import DeleteUserByID
from src.applications.usecases.delete_user_by_id.delete_user_by_id_presenter_interface import \
    DeleteUserByIDPresenterInterface
from src.applications.usecases.delete_user_by_id.delete_user_by_id_gateway import DeleteUserByIDGateway


class TestDeleteUserByID(TestCase):
    def setUp(self) -> None:
        self.repository = DeleteUserByIDRepository()
        self.delete_by_id = DeleteUserByID(repository=self.repository)
        self.presenter = DeleteUserByIDPresenter()

    def test_if_delete_by_id_is_instance_of(self):
        self.assertIsInstance(self.delete_by_id, DeleteUserByID)

    def test_if_delete_by_id_return_value_true(self):
        self.delete_by_id.execute(id="123456", presenter=self.presenter)
        self.assertTrue(self.presenter.get_view_model())

    def tearDown(self) -> None:
        self.repository = None
        self.delete_by_id = None
        self.presenter = None


class DeleteUserByIDRepository(DeleteUserByIDGateway):
    def delete_user_by_id(self, id: str) -> bool():
        return True

    def delete_user_by_username(self, username: str) -> bool():
        return True


class DeleteUserByIDPresenter(DeleteUserByIDPresenterInterface):
    def __init__(self):
        self.value: bool = False

    def present(self, value: bool):
        self.value = value

    def get_view_model(self):
        return self.value
