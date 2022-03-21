from unittest import TestCase

import bcrypt

from domain.src.gateweys.registration_gateway import RegistrationGateway
from domain.src.interfaces.registration_interface import RegistrationInterface
from domain.src.interfaces.registration_presenter_interface import RegistrationPresenterInterface
from src.applications.usecases.user_registration.registration_input_boundary import RegistrationInputBoundary
from src.applications.usecases.user_registration.registration_output_boundary import RegistrationOutputBoundary
from src.applications.usecases.user_registration.registration_output_interface import RegistrationOutputInterface
from src.applications.usecases.user_registration.user_registration import UserRegistration


class TestUserRegistration(TestCase):
    def setUp(self) -> None:
        self.registration = None
        self.repository: RegistrationGateway = RegistrationRepository()
        self.username: str = "jackson"
        self.email: str = "jacksonsr45@gmail.com"
        self.password: str = "123456"

    def test_if_registration_is_instance_of(self):
        self.registration = UserRegistration(repository=self.repository)
        self.assertIsInstance(self.registration, UserRegistration)

    def test_if_registration_execute_and_return_values(self):
        self.registration = UserRegistration(repository=self.repository)
        registration_input = RegistrationInputBoundary(username=self.username, email=self.email, password=self.password)
        presenter = RegistrationPresenter()
        self.registration.execute(registration_input=registration_input, presenter=presenter)

        self.assertTrue(presenter.get_view_model().result)

    def tearDown(self) -> None:
        self.registration = None
        self.repository = None


class RegistrationRepository(RegistrationGateway):
    def insert_new_user(self, registration: RegistrationInterface) -> bool():
        return True


class RegistrationPresenter(RegistrationPresenterInterface):
    def __init__(self):
        self.view_model: RegistrationViewModel = None

    def present(self, registration: bool):
        self.view_model = RegistrationViewModel(registration=registration)

    def get_view_model(self):
        return self.view_model


class RegistrationViewModel:
    def __init__(self, registration: bool):
        self.result: bool = registration
