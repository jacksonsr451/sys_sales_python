from src.applications.usecases.list_users.list_users_gateway import ListUsersGateway
from src.applications.usecases.list_users.list_users_presenter_interface import ListUsersPresenterInterface


class ListUsers:
    def __init__(self, repository: ListUsersGateway):
        self.repository = repository

    def list(self, presenter: ListUsersPresenterInterface):
        presenter.present(self.repository.list_users())
