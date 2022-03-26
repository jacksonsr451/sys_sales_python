from src.applications.usecases.register_user.register_user_presenter_interface import RegisterUserPresenterInterface
from src.applications.usecases.register_user.register_user_input_boundary import RegisterUserInputBoundary
from src.applications.usecases.register_user.register_user import UserRegistration
from src.infrastructure.repositories.users_repository import UserRepositoryByID


class RegistrationController:
    def __init__(self, request, repository: UserRepositoryByID):
        self.request = request
        self.registration = UserRegistration(repository=repository)

    def register(self, presenter: RegisterUserPresenterInterface):
        registration_input = RegisterUserInputBoundary(
            username=self.request['username'],
            password=self.request['password'],
            email=self.request['email']
        )
        self.registration.execute(registration_input=registration_input, presenter=presenter)
