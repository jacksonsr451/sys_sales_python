from abc import ABC, abstractmethod


class RegisterUserInputInterface(ABC):
    @abstractmethod
    def get_username(self) -> str:
        print("This method is required")

    @abstractmethod
    def get_email(self) -> str:
        print("This method is required")

    @abstractmethod
    def get_password(self) -> str:
        print("This method is required")