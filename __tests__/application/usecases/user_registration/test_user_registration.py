from unittest import TestCase

from domain.src.interfaces.register_user_entity_interface import RegisterUserEntityInterface
from src.applications.usecases.register_user.register_user_presenter_interface import RegisterUserPresenterInterface
from src.applications.usecases.register_user.register_user_input_boundary import RegisterUserInputBoundary
from src.applications.usecases.register_user.register_user import UserRegistration
from src.interface.gateweys.register_user_gateway import RegisterUserGateway


class TestUserRegistration(TestCase):
    def setUp(self) -> None:
        self.registration = None
        self.repository: RegisterUserGateway = RegisterUserRepository()
        self.username: str = "jackson"
        self.email: str = "jacksonsr45@gmail.com"
        self.password: str = "123456"

    def test_if_registration_is_instance_of(self):
        self.registration = UserRegistration(repository=self.repository)
        self.assertIsInstance(self.registration, UserRegistration)

    def test_if_registration_execute_and_return_values(self):
        self.registration = UserRegistration(repository=self.repository)
        registration_input = RegisterUserInputBoundary(username=self.username, email=self.email, password=self.password)
        presenter = RegisterUserPresenter()
        self.registration.execute(registration_input=registration_input, presenter=presenter)

        self.assertTrue(presenter.get_view_model().result)

    def tearDown(self) -> None:
        self.registration = None
        self.repository = None


class RegisterUserRepository(RegisterUserGateway):
    def insert_new_user(self, registration: RegisterUserEntityInterface) -> bool():
        return True


class RegisterUserPresenter(RegisterUserPresenterInterface):
    def __init__(self):
        self.view_model: RegistrationViewModel = None

    def present(self, registration: bool):
        self.view_model = RegistrationViewModel(registration=registration)

    def get_view_model(self):
        return self.view_model


class RegistrationViewModel:
    def __init__(self, registration: bool):
        self.result: bool = registration
