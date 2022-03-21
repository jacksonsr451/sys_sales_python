from abc import ABC, abstractmethod


class HashPasswordInterface(ABC):
    @abstractmethod
    def encrypt(self, password: str) -> str:
        print("This method is required")
