from domain.src.interfaces.registration_presenter_interface import RegistrationPresenterInterface
from src.applications.usecases.user_registration.registration_input_boundary import RegistrationInputBoundary
from src.applications.usecases.user_registration.user_registration import UserRegistration
from src.infrastructure.repositories.users_repository import UsersRepository


class RegistrationController:
    def __init__(self, request, repository: UsersRepository):
        self.request = request
        self.registration = UserRegistration(repository=repository)

    def register(self, presenter: RegistrationPresenterInterface):
        registration_input = RegistrationInputBoundary(
            username=self.request['username'],
            password=self.request['password'],
            email=self.request['email']
        )
        self.registration.execute(registration_input=registration_input, presenter=presenter)
