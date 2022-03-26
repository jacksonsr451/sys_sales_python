from domain.src.interfaces.delete_user_interface import DeleteUserInterface
from domain.src.interfaces.delete_user_input_interface import DeleteUserInputInterface
from domain.src.object_values.user_id import UserID
from domain.src.object_values.user_id_interface import UserIDInterface


class DeleteUserEntity(DeleteUserInterface):
    def __init__(self, delete_input: DeleteUserInputInterface):
        self.__id: UserIDInterface = UserID(delete_input.get_id())

    def get_id(self) -> str:
        return self.__id.get_id()
