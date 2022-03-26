from abc import ABC, abstractmethod


class UserEmailInterface(ABC):
    @abstractmethod
    def get_email(self) -> str:
        print("This method is required")
