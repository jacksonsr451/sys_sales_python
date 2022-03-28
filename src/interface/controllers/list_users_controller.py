from src.applications.usecases.list_users.list_users_presenter_interface import ListUsersPresenterInterface
from src.infrastructure.repositories.users_repository import UserRepository


class ListUsersController:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def list(self, presenter: ListUsersPresenterInterface):
        presenter.present(self.repository.list_users())
