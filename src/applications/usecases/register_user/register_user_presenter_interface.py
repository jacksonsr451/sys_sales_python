from abc import ABC, abstractmethod


class RegisterUserPresenterInterface(ABC):
    @abstractmethod
    def present(self, registration: bool):
        print("This method is required!")

    @abstractmethod
    def get_view_model(self):
        print("This method is required!")
