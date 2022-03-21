from abc import ABC, abstractmethod


class RegisterUsernameInterface(ABC):
    @abstractmethod
    def get_username(self) -> str:
        print("This method is required")
