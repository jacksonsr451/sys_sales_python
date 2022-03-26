from unittest import TestCase

from app.app import create_app
from app.extensions.flask_sqlalchemy import data_base
from domain.src.entities.register_user_entity import RegisterUserEntity
from src.applications.usecases.register_user.register_user_input_boundary import RegisterUserInputBoundary
from src.infrastructure.exceptions.insert_exception import InsertException
from src.infrastructure.repositories.users_repository import UserRepositoryByID


class TestUsersRepository(TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        with self.app.app_context():
            data_base.create_all(app=self.app)
        self.repository = UserRepositoryByID()
        self.username: str = "jackson"
        self.email: str = "jacksonsr45@gmail.com"
        self.password: str = "123456"

    def test_if_repository_is_instance_of(self):
        self.assertIsInstance(self.repository, UserRepositoryByID)

    def test_if_repository_insert_new_user(self):
        input_register = RegisterUserInputBoundary(username=self.username, email=self.email, password=self.password)
        registration = RegisterUserEntity(register=input_register)

        self.assertTrue(self.repository.insert_new_user(registration=registration))
        self.assertTrue(self.repository.delete_user_by_id(id=registration.get_id()))

    def test_if_repository_return_error_insert_exception(self):
        input_register = RegisterUserInputBoundary(username=self.username, email=self.email, password=self.password)
        with self.assertRaises(InsertException) as context:
            registration = RegisterUserEntity(register=input_register)
            self.repository.insert_new_user(registration=registration)
            self.repository.insert_new_user(registration=registration)
        self.assertEqual('Insert error in table: users', context.exception.message)
        self.assertTrue(self.repository.delete_user_by_id(id=registration.get_id()))

    def tearDown(self) -> None:
        self.repository = None
        self.username: str = ""
        self.email: str = ""
        self.password: str = ""
