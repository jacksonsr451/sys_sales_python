from unittest import TestCase

from domain.src.entities.delete_user_entity import DeleteUserEntity
from domain.src.interfaces.delete_user_input_interface import DeleteUserInputInterface


class TestDeleteUserEntity(TestCase):
    def setUp(self) -> None:
        self.input: DeleteUserInputInterface = DeleteUserInput("123456789")
        self.delete = DeleteUserEntity(self.input)

    def test_if_delete_is_instance_of(self):
        self.assertIsInstance(self.delete, DeleteUserEntity)

    def test_if_delete_get_return_of_id(self):
        self.assertEqual(self.input.get_id(), self.delete.get_id())

    def tearDown(self) -> None:
        self.input = None
        self.delete = None


class DeleteUserInput(DeleteUserInputInterface):
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
