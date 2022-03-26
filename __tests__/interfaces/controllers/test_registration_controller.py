from dataclasses import fields
from unittest import TestCase

from app.app import create_app
from app.extensions.flask_sqlalchemy import data_base
from src.infrastructure.repositories.users_repository import UsersRepository
from src.interface.controllers.registration_controller import RegistrationController
from src.interface.presenters.registration_presenter import RegisterUserPresenter


class TestRegistrationController(TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        with self.app.app_context():
            data_base.create_all(app=self.app)
        self.repository = UsersRepository()
        self.request = {
            "username": "jackson",
            "password": "123456",
            "email": "jacksonsr45@gmail.com"
        }
        self.controller = None
        self.presenter = RegisterUserPresenter()

    def test_if_controller_is_instance_of(self):
        self.controller = RegistrationController(request=self.request, repository=self.repository)
        self.assertIsInstance(self.controller, RegistrationController)

    def test_if_controller_execute_insert_data_in_db(self):
        self.controller = RegistrationController(request=self.request, repository=self.repository)
        self.controller.register(presenter=self.presenter)
        value, code = self.presenter.get_view_model()

        self.assertTrue(value)
        self.assertTrue(code, 200)
        self.assertTrue(self.repository.delete_user_by_username(username=self.request["username"]))

    def tearDown(self) -> None:
        self.repository = None
        self.request = None
        self.controller = None
        self.presenter = None
