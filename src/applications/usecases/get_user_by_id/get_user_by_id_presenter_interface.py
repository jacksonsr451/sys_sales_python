from abc import abstractmethod, ABC


class GetUserByIDPresenterInterface(ABC):
    @abstractmethod
    def present(self, user):
        print("This method is required!")

    @abstractmethod
    def get_view_model(self):
        print("This method is required!")
