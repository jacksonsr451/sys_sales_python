from src.applications.usecases.list_users.list_users_presenter_interface import ListUsersPresenterInterface


class ListUsersPresenter(ListUsersPresenterInterface):
    def __init__(self):
        self.users: list = list()

    def present(self, list_users: list):
        self.users = list_users

    def get_view_model(self):
        return self.users
