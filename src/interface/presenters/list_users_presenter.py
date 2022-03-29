from src.applications.usecases.list_users.list_users_presenter_interface import ListUsersPresenterInterface


class ListUsersPresenter(ListUsersPresenterInterface):
    def __init__(self):
        self.users = None
        self.code = 400

    def present(self, list_users=None):
        self.users = list_users

    def get_view_model(self):
        if self.users is not None:
            self.code = 202
        return self.users, self.code
