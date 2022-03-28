from abc import ABC, abstractmethod


class DeleteUserByIDGateway(ABC):
    @abstractmethod
    def delete_user_by_id(self, id: str) -> bool():
        print("This method is required!")

    @abstractmethod
    def delete_user_by_username(self, username: str) -> bool():
        print("This method is required!")
        