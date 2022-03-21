from unittest import TestCase

import bcrypt

from domain.src.exceptions.email_register_exception import EmailRegisterException
from domain.src.exceptions.password_register_exception import PasswordRegisterException
from domain.src.exceptions.username_register_exception import UsernameRegisterException
from domain.src.entities.registration import Registration
from domain.src.interfaces.registration_interface import RegistrationInterface
from src.applications.usecases.user_registration.registration_input_boundary import RegistrationInputBoundary


class TestRegistration(TestCase):
    def setUp(self) -> None:
        self.registration: RegistrationInterface = None
        self.username: str = "jackson"
        self.email: str = "jacksonsr45@gmail.com"
        self.password: str = "123456"

    def test_if_registration_is_instance_of(self):
        register = RegistrationInputBoundary(username="jackson", email="jacksonsr45@gmail.com", password="123456")
        self.registration = Registration(register=register)
        self.assertIsInstance(self.registration, Registration)

    def test_if_has_exception_on_username_is_invalid(self):
        self.username = "jack"
        register = RegistrationInputBoundary(username=self.username, email=self.email, password=self.password)
        with self.assertRaises(UsernameRegisterException) as context:
            Registration(register=register)
        self.assertEqual('Username is invalid format, required at least six characters!', context.exception.message)

    def test_if_has_exception_on_email_is_invalid(self):
        self.email = "jacksonsr45@gmail"
        register = RegistrationInputBoundary(username=self.username, email=self.email, password=self.password)
        with self.assertRaises(EmailRegisterException) as context:
            Registration(register=register)
        self.assertEqual('Email is invalid format!', context.exception.message)

    def test_if_has_exception_on_password_is_invalid(self):
        self.password = "1234"
        register = RegistrationInputBoundary(username=self.username, email=self.email, password=self.password)
        with self.assertRaises(PasswordRegisterException) as context:
            Registration(register=register)
        self.assertEqual('Password is invalid format, required at least six characters!', context.exception.message)

    def test_if_registration_return_values_creating_correct(self):
        register = RegistrationInputBoundary(username=self.username, password=self.password, email=self.email)
        self.registration = Registration(register=register)

        self.assertIsNotNone(self.registration.get_id())
        self.assertEqual(self.username, self.registration.get_username())
        self.assertTrue(bcrypt.checkpw(self.password.encode('utf8'), self.registration.get_password().encode('utf8')))
        self.assertEqual(self.email, self.registration.get_email())

    def tearDown(self) -> None:
        self.registration = None
