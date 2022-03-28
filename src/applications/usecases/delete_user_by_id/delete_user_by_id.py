from src.applications.usecases.delete_user_by_id.delete_user_by_id_presenter_interface import DeleteUserByIDPresenterInterface
from src.applications.usecases.delete_user_by_id.delete_user_by_id_gateway import DeleteUserByIDGateway


class DeleteUserByID:
    def __init__(self, repository: DeleteUserByIDGateway):
        self.repository: DeleteUserByIDGateway = repository

    def execute(self, id: str, presenter: DeleteUserByIDPresenterInterface):
        presenter.present(self.repository.delete_user_by_id(id=id))
