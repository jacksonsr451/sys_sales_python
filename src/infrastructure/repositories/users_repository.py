from domain.src.gateweys.registration_gateway import RegistrationGateway
from domain.src.interfaces.registration_interface import RegistrationInterface
from src.infrastructure.models.model_factoring import ModelFactoring
from src.infrastructure.models.user_model import UserModel


class UsersRepository(
    RegistrationGateway
):
    def __init__(self):
        self.users: ModelFactoring = UserModel()

    def insert_new_user(self, registration: RegistrationInterface) -> bool():
        return self.users.insert(
            ["id", "username", "password", "email"],
            [registration.get_id(), registration.get_username(), registration.get_password(), registration.get_email()]
        )

    def delete_user(self, where: list, values: list) -> bool():
        return self.users.delete(where=where, values=values)
