from domain.src.interfaces.register_user_entity_interface import RegisterUserEntityInterface
from src.applications.usecases.user_registration.registration_output_interface import RegistrationOutputInterface


class RegistrationOutputBoundary(RegistrationOutputInterface):
    def __init__(self, register: RegisterUserEntityInterface):
        self.__username: str = register.get_username()
        self.__email: str = register.get_email()
        self.__id: str = register.get_id()

    def get_username(self) -> str:
        return self.__username

    def get_email(self) -> str:
        return self.__email

    def get_id(self) -> str:
        return self.__id
