from unittest import TestCase

from domain.src.entities.delete_user_by_id_entity import DeleteUserByIDByIDEntity
from domain.src.interfaces.delete_user_by_id_input_interface import DeleteUserByIDInputInterface


class TestDeleteUserEntity(TestCase):
    def setUp(self) -> None:
        self.input: DeleteUserByIDInputInterface = DeleteUserByIDInput("123456789")
        self.delete = DeleteUserByIDByIDEntity(self.input)

    def test_if_delete_is_instance_of(self):
        self.assertIsInstance(self.delete, DeleteUserByIDByIDEntity)

    def test_if_delete_get_return_of_id(self):
        self.assertEqual(self.input.get_id(), self.delete.get_id())

    def tearDown(self) -> None:
        self.input = None
        self.delete = None


class DeleteUserByIDInput(DeleteUserByIDInputInterface):
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
