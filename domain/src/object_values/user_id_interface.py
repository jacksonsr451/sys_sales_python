from abc import ABC, abstractmethod


class UserIDInterface(ABC):
    @abstractmethod
    def get_id(self):
        print("This method is required!")
