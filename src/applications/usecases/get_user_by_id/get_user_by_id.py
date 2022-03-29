from src.applications.usecases.get_user_by_id.get_user_by_id_gateway import GetUserByIDGateway


class GetUserByID:
    def __init__(self, repository: GetUserByIDGateway):
        self.repository: GetUserByIDGateway = repository

    def get_user(self, id: str, presenter):
        presenter.present(self.repository.get_user_by_id(id=id))
