from abc import ABC, abstractmethod


class RegisterEmailInterface(ABC):
    @abstractmethod
    def get_email(self) -> str:
        print("This method is required")
