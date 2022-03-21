from domain.src.exceptions.password_register_exception import PasswordRegisterException
from domain.src.interfaces.hash_password_interface import HashPasswordInterface
from domain.src.object_values.register_password_interface import RegisterPasswordInterface


class RegisterRegisterPassword(RegisterPasswordInterface):
    def __init__(self, password: str):
        if not self.__validate(password=password):
            raise PasswordRegisterException()
        self.password = password

    @classmethod
    def __validate(cls, password) -> bool():
        if len(password) < 6:
            return False
        return True

    def get_password(self, hash_password: HashPasswordInterface) -> str:
        return hash_password.encrypt(self.password)
