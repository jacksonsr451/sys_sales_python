from abc import ABC, abstractmethod


class DeleteUserInterface(ABC):
    @abstractmethod
    def get_id(self) -> str:
        print("This method is required!")
