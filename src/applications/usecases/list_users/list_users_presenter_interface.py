from abc import ABC, abstractmethod


class ListUsersPresenterInterface(ABC):
    @abstractmethod
    def present(self, list_users: list):
        print("This method is required")

    @abstractmethod
    def get_view_model(self):
        print("This method is required")
