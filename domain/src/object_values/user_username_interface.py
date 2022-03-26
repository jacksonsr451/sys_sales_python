from abc import ABC, abstractmethod


class UserUsernameInterface(ABC):
    @abstractmethod
    def get_username(self) -> str:
        print("This method is required")
