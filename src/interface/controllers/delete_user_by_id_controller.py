from src.applications.usecases.delete_user_by_id.delete_user_by_id import DeleteUserByID
from src.applications.usecases.delete_user_by_id.delete_user_by_id_presenter_interface import \
    DeleteUserByIDPresenterInterface
from src.infrastructure.repositories.users_repository import UserRepositoryByID


class DeleteUserByIDController:
    def __init__(self, request, repository: UserRepositoryByID):
        self.request = request
        self.delete_user = DeleteUserByID(repository=repository)

    def delete(self, presenter: DeleteUserByIDPresenterInterface):
        self.delete_user.execute(id=self.request['id'], presenter=presenter)
