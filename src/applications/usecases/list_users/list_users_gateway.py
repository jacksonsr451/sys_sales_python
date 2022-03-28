from abc import ABC, abstractmethod


class ListUsersGateway(ABC):
    @abstractmethod
    def list_users(self) -> list:
        print("This method is required")
