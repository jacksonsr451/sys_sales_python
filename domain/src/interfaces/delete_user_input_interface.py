from abc import ABC, abstractmethod


class DeleteUserInputInterface(ABC):
    @abstractmethod
    def get_id(self):
        print("This method is required!")
