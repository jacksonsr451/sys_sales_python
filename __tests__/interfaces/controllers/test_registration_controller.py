from dataclasses import fields
from unittest import TestCase

from src.infrastructure.repositories.users_repository import UsersRepository
from src.interface.controllers.registration_controller import RegistrationController
from src.interface.presenters.registration_presenter import RegistrationPresenter


class TestRegistrationController(TestCase):
    def setUp(self) -> None:
        self.repository = UsersRepository()
        self.request = {
            "username": "jackson",
            "password": "123456",
            "email": "jacksonsr45@gmail.com"
        }
        self.controller = None
        self.presenter = RegistrationPresenter()

    def test_if_controller_is_instance_of(self):
        self.controller = RegistrationController(request=self.request, repository=self.repository)
        self.assertIsInstance(self.controller, RegistrationController)

    def test_if_controller_execute_insert_data_in_db(self):
        self.controller = RegistrationController(request=self.request, repository=self.repository)
        self.controller.register(presenter=self.presenter)
        value, code = self.presenter.get_view_model()

        self.assertTrue(value)
        self.assertTrue(code, 200)
        self.assertTrue(self.repository.delete_user(where=["username"], values=[self.request["username"]]))

    def tearDown(self) -> None:
        self.repository = None
        self.request = None
        self.controller = None
        self.presenter = None
