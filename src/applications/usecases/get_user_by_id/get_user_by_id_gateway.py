from abc import ABC, abstractmethod


class GatUserByIDGateway(ABC):
    @abstractmethod
    def get_user_by_id(self, id: str):
        print("This method is required!")
