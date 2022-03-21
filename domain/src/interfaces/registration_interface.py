from abc import ABC, abstractmethod


class RegistrationInterface(ABC):
    @abstractmethod
    def get_id(self) -> str:
        print("This method is required")

    @abstractmethod
    def get_username(self) -> str:
        print("This method is required")

    @abstractmethod
    def get_email(self) -> str:
        print("This method is required")

    @abstractmethod
    def get_password(self) -> str:
        print("This method is required")
