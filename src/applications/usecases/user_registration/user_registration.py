from domain.src.entities.registration import Registration
from domain.src.gateweys.registration_gateway import RegistrationGateway
from domain.src.interfaces.registration_presenter_interface import RegistrationPresenterInterface
from src.applications.usecases.user_registration.registration_input_interface import RegistrationInputInterface


class UserRegistration:
    def __init__(self, repository: RegistrationGateway):
        self.repository: RegistrationGateway = repository

    def execute(self, registration_input: RegistrationInputInterface, presenter: RegistrationPresenterInterface):
        presenter.present(self.repository.insert_new_user(Registration(registration_input)))
