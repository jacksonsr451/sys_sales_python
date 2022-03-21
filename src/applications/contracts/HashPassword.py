import bcrypt

from domain.src.interfaces.hash_password_interface import HashPasswordInterface


class HashPassword(HashPasswordInterface):
    def __init__(self):
        self.hashed = None

    def encrypt(self, password: str) -> str:
        self.hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        return self.hashed.decode('utf8')
