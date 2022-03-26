from domain.src.exceptions.username_register_exception import UsernameRegisterException
from domain.src.object_values.user_username_interface import UserUsernameInterface


class UserUserUsername(UserUsernameInterface):
    def __init__(self, username: str):
        if not self.__validate(username):
            raise UsernameRegisterException()
        self.username: str = username

    @classmethod
    def __validate(cls, username: str) -> bool:
        if len(username) < 6:
            return False
        return True

    def get_username(self) -> str:
        return self.username
