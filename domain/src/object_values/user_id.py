import uuid

from domain.src.exceptions.user_id_required_str_exception import UserIDRequiredSTRException
from domain.src.object_values.user_id_interface import UserIDInterface


class UserID(UserIDInterface):
    def __init__(self, id=None):
        if id is not None and type(id) is not str:
            raise UserIDRequiredSTRException
        if id is not None:
            self.__id = id
        else:
            self.__id = str(uuid.uuid4())

    def get_id(self) -> str:
        return self.__id
