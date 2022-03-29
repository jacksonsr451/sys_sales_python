from src.applications.usecases.get_user_by_id.get_user_by_id_gateway import GatUserByIDGateway


class GetUserByID:
    def __init__(self, repository: GatUserByIDGateway):
        self.repository: GatUserByIDGateway = repository

    def get_user(self, id: str, presenter):
        presenter.present(self.repository.get_user_by_id(id=id))
