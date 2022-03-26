import uuid

from domain.src.object_values.user_email import UserUserEmail
from domain.src.object_values.user_email_interface import UserEmailInterface
from domain.src.object_values.user_password import UserUserPassword
from domain.src.object_values.user_password_interface import UserPasswordInterface
from domain.src.object_values.user_username import UserUserUsername
from domain.src.object_values.user_username_interface import UserUsernameInterface
from domain.src.interfaces.register_user_entity_interface import RegisterUserEntityInterface
from domain.src.object_values.user_id import UserID
from domain.src.object_values.user_id_interface import UserIDInterface
from src.applications.contracts.HashPassword import HashPassword
from src.applications.usecases.user_registration.registration_input_interface import RegistrationInputInterface


class RegisterUserEntity(RegisterUserEntityInterface):
    def __init__(self, register: RegistrationInputInterface):
        self.__username: UserUsernameInterface = UserUserUsername(username=register.get_username())
        self.__email: UserEmailInterface = UserUserEmail(email=register.get_email())
        self.__password: UserPasswordInterface = UserUserPassword(password=register.get_password())
        self.__id: UserIDInterface = UserID()

    def get_id(self) -> str:
        return self.__id.get_id()

    def get_username(self) -> str:
        return self.__username.get_username()

    def get_email(self) -> str:
        return self.__email.get_email()

    def get_password(self) -> str:
        return self.__password.get_password(HashPassword())
