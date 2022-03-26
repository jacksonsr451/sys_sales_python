from unittest import TestCase

import bcrypt

from domain.src.exceptions.email_register_exception import EmailRegisterException
from domain.src.exceptions.password_register_exception import PasswordRegisterException
from domain.src.exceptions.username_register_exception import UsernameRegisterException
from domain.src.entities.register_user_entity import RegisterUserEntity
from domain.src.interfaces.register_user_entity_interface import RegisterUserEntityInterface
from src.applications.usecases.register_user.register_user_input_boundary import RegisterUserInputBoundary


class TestRegistration(TestCase):
    def setUp(self) -> None:
        self.registration: RegisterUserEntityInterface = None
        self.username: str = "jackson"
        self.email: str = "jacksonsr45@gmail.com"
        self.password: str = "123456"

    def test_if_registration_is_instance_of(self):
        register = RegisterUserInputBoundary(username="jackson", email="jacksonsr45@gmail.com", password="123456")
        self.registration = RegisterUserEntity(register=register)
        self.assertIsInstance(self.registration, RegisterUserEntity)

    def test_if_has_exception_on_username_is_invalid(self):
        self.username = "jack"
        register = RegisterUserInputBoundary(username=self.username, email=self.email, password=self.password)
        with self.assertRaises(UsernameRegisterException) as context:
            RegisterUserEntity(register=register)
        self.assertEqual('Username is invalid format, required at least six characters!', context.exception.message)

    def test_if_has_exception_on_email_is_invalid(self):
        self.email = "jacksonsr45@gmail"
        register = RegisterUserInputBoundary(username=self.username, email=self.email, password=self.password)
        with self.assertRaises(EmailRegisterException) as context:
            RegisterUserEntity(register=register)
        self.assertEqual('Email is invalid format!', context.exception.message)

    def test_if_has_exception_on_password_is_invalid(self):
        self.password = "1234"
        register = RegisterUserInputBoundary(username=self.username, email=self.email, password=self.password)
        with self.assertRaises(PasswordRegisterException) as context:
            RegisterUserEntity(register=register)
        self.assertEqual('Password is invalid format, required at least six characters!', context.exception.message)

    def test_if_registration_return_values_creating_correct(self):
        register = RegisterUserInputBoundary(username=self.username, password=self.password, email=self.email)
        self.registration = RegisterUserEntity(register=register)

        self.assertIsNotNone(self.registration.get_id())
        self.assertEqual(self.username, self.registration.get_username())
        self.assertTrue(bcrypt.checkpw(self.password.encode('utf8'), self.registration.get_password().encode('utf8')))
        self.assertEqual(self.email, self.registration.get_email())

    def tearDown(self) -> None:
        self.registration = None
