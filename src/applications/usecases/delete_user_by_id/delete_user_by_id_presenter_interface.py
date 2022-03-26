from abc import ABC, abstractmethod


class DeleteUserByIDPresenterInterface(ABC):
    @abstractmethod
    def present(self, value: bool):
        print("This method is required!")

    @abstractmethod
    def get_view_model(self):
        print("This method is required!")
