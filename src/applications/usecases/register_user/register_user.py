from domain.src.entities.register_user_entity import RegisterUserEntity
from domain.src.gateweys.register_user_gateway import RegisterUserGateway
from src.applications.usecases.register_user.register_user_presenter_interface import RegisterUserPresenterInterface
from domain.src.interfaces.register_user_input_interface import RegisterUserInputInterface


class UserRegistration:
    def __init__(self, repository: RegisterUserGateway):
        self.repository: RegisterUserGateway = repository

    def execute(self, registration_input: RegisterUserInputInterface, presenter: RegisterUserPresenterInterface):
        presenter.present(self.repository.insert_new_user(RegisterUserEntity(registration_input)))
