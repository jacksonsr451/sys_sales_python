from abc import ABC, abstractmethod


class ConnectDBInterface(ABC):
    @abstractmethod
    def connect(self):
        print("This method is required")
