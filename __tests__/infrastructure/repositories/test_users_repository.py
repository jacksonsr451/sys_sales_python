from unittest import TestCase

from app.app import create_app
from app.extensions.flask_sqlalchemy import data_base
from domain.src.entities.registration import Registration
from src.applications.usecases.user_registration.registration_input_boundary import RegistrationInputBoundary
from src.infrastructure.repositories.users_repository import UsersRepository


class TestUsersRepository(TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        with self.app.app_context():
            data_base.create_all(app=self.app)
        self.repository = UsersRepository()
        self.username: str = "jackson"
        self.email: str = "jacksonsr45@gmail.com"
        self.password: str = "123456"

    def test_if_repository_is_instance_of(self):
        self.assertIsInstance(self.repository, UsersRepository)

    def test_if_repository_insert_new_user(self):
        input_register = RegistrationInputBoundary(username=self.username, email=self.email, password=self.password)
        registration = Registration(register=input_register)

        self.assertTrue(self.repository.insert_new_user(registration=registration))
        self.assertTrue(self.repository.delete_user_by_id(id=registration.get_id()))

    # def test_if_repository_return_error_insert_exception(self):
    #     input_register = RegistrationInputBoundary(username=self.username, email=self.email, password=self.password)
    #
    #     with self.assertRaises(InsertException) as context:
    #         registration = Registration(register=input_register)
    #         self.repository.insert_new_user(registration=registration)
    #         self.repository.insert_new_user(registration=registration)
    #     self.assertEqual('Insert error in table: users', context.exception.message)
    #     self.assertTrue(self.repository.delete_user_by_id(id=registration.get_id()))

    def tearDown(self) -> None:
        self.repository = None
        self.username: str = ""
        self.email: str = ""
        self.password: str = ""
