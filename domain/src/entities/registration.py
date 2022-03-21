import uuid

from domain.src.object_values.register_email import RegisterRegisterEmail
from domain.src.object_values.register_email_interface import RegisterEmailInterface
from domain.src.object_values.register_password import RegisterRegisterPassword
from domain.src.object_values.register_password_interface import RegisterPasswordInterface
from domain.src.object_values.register_username import RegisterRegisterUsername
from domain.src.object_values.register_username_interface import RegisterUsernameInterface
from domain.src.interfaces.registration_interface import RegistrationInterface
from src.applications.contracts.HashPassword import HashPassword
from src.applications.usecases.user_registration.registration_input_interface import RegistrationInputInterface


class Registration(RegistrationInterface):
    def __init__(self, register: RegistrationInputInterface):
        self.__username: RegisterUsernameInterface = RegisterRegisterUsername(username=register.get_username())
        self.__email: RegisterEmailInterface = RegisterRegisterEmail(email=register.get_email())
        self.__password: RegisterPasswordInterface = RegisterRegisterPassword(password=register.get_password())
        self.__id: str = str(uuid.uuid4())

    def get_id(self) -> str:
        return self.__id

    def get_username(self) -> str:
        return self.__username.get_username()

    def get_email(self) -> str:
        return self.__email.get_email()

    def get_password(self) -> str:
        return self.__password.get_password(HashPassword())
