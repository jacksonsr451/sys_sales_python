from src.applications.usecases.get_user_by_id.get_user_by_id_gateway import GetUserByIDGateway
from src.applications.usecases.get_user_by_id.get_user_by_id_presenter_interface import GetUserByIDPresenterInterface


class GetUserByIDController:
    def __init__(self, repository: GetUserByIDGateway):
        self.repository = repository

    def get_user(self, id: str, presenter: GetUserByIDPresenterInterface):
        presenter.present(self.repository.get_user_by_id(id=id))
