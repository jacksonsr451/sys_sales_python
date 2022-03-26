from domain.src.entities.register_user_entity import RegisterUserEntity
from domain.src.gateweys.register_user_gateway import RegisterUserGateway
from domain.src.interfaces.registration_presenter_interface import RegistrationPresenterInterface
from src.applications.usecases.user_registration.registration_input_interface import RegistrationInputInterface


class UserRegistration:
    def __init__(self, repository: RegisterUserGateway):
        self.repository: RegisterUserGateway = repository

    def execute(self, registration_input: RegistrationInputInterface, presenter: RegistrationPresenterInterface):
        presenter.present(self.repository.insert_new_user(RegisterUserEntity(registration_input)))
