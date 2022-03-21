from domain.src.interfaces.registration_interface import RegistrationInterface
from src.applications.usecases.user_registration.registration_output_interface import RegistrationOutputInterface


class RegistrationOutputBoundary(RegistrationOutputInterface):
    def __init__(self, register: RegistrationInterface):
        self.__username: str = register.get_username()
        self.__email: str = register.get_email()
        self.__id: str = register.get_id()

    def get_username(self) -> str:
        return self.__username

    def get_email(self) -> str:
        return self.__email

    def get_id(self) -> str:
        return self.__id
