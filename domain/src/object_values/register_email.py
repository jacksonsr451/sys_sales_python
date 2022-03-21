import re

from domain.src.exceptions.email_register_exception import EmailRegisterException
from domain.src.object_values.register_email_interface import RegisterEmailInterface


class RegisterRegisterEmail(RegisterEmailInterface):
    def __init__(self, email):
        self.regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not self.__validate(email):
            raise EmailRegisterException()
        self.email: str = email

    def __validate(self, email: str) -> bool():
        if not re.search(self.regex, email):
            return False
        return True

    def get_email(self) -> str:
        return self.email
