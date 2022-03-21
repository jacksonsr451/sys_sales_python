from abc import ABC, abstractmethod

from domain.src.interfaces.hash_password_interface import HashPasswordInterface


class RegisterPasswordInterface(ABC):
    @abstractmethod
    def get_password(self, hash_password: HashPasswordInterface) -> str:
        print("This method is required")
