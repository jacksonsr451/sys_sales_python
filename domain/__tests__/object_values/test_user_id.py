from unittest import TestCase

from domain.src.exceptions.user_id_required_str_exception import UserIDRequiredSTRException
from domain.src.object_values.user_id import UserID
from domain.src.object_values.user_id_interface import UserIDInterface


class TestUserID(TestCase):
    def setUp(self) -> None:
        self.user_id: UserIDInterface = None

    def test_if_user_id_is_instance_of(self):
        self.user_id = UserID("123456789")
        self.assertIsInstance(self.user_id, UserID)

    def test_if_user_id_return_exception(self):
        with self.assertRaises(UserIDRequiredSTRException) as context:
            UserID(123456789)
        self.assertEqual('User ID required type String', context.exception.message)

    def tearDown(self) -> None:
        self.user_id = None
