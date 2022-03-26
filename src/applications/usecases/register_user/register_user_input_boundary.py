from domain.src.interfaces.register_user_input_interface import RegisterUserInputInterface


class RegisterUserInputBoundary(RegisterUserInputInterface):
    def __init__(self, username: str, email: str, password: str):
        self.__username: str = username
        self.__email: str = email
        self.__password: str = password

    def get_username(self) -> str:
        return self.__username

    def get_email(self) -> str:
        return self.__email

    def get_password(self) -> str:
        return self.__password
