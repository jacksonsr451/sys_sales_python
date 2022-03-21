from abc import ABC, abstractmethod

from domain.src.interfaces.registration_interface import RegistrationInterface


class RegistrationGateway(ABC):
    @abstractmethod
    def insert_new_user(self, registration: RegistrationInterface) -> bool():
        print("This method is required!")
