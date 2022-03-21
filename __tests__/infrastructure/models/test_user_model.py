from unittest import TestCase

from src.infrastructure.models.user_model import UserModel


class TestUserModel(TestCase):
    def setUp(self) -> None:
        self.user = UserModel()

    def test_if_user_model_is_instance_of(self):
        self.assertIsInstance(self.user, UserModel)

    def tearDown(self) -> None:
        pass
