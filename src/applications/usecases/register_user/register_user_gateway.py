from abc import ABC, abstractmethod

from domain.src.interfaces.register_user_entity_interface import RegisterUserEntityInterface


class RegisterUserGateway(ABC):
    @abstractmethod
    def insert_new_user(self, registration: RegisterUserEntityInterface) -> bool():
        print("This method is required!")
