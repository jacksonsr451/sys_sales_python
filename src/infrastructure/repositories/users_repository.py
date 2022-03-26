from sqlite3 import Error

from flask_sqlalchemy import Model

from app.extensions.flask_sqlalchemy import data_base
from domain.src.gateweys.registration_gateway import RegistrationGateway
from domain.src.interfaces.registration_interface import RegistrationInterface
from src.infrastructure.models.user_model import UserModel


class UsersRepository(
    RegistrationGateway
):
    def __init__(self):
        self.users: Model = UserModel()

    def insert_new_user(self, registration: RegistrationInterface) -> bool():
        try:
            data = {
                "id": registration.get_id(),
                "username": registration.get_username(),
                "email": registration.get_email(),
                "password": registration.get_password()
            }
            self.users = UserModel(data=data)
            data_base.session.add(self.users)
            data_base.session.commit()
            return True
        except Error:
            return False

    def delete_user_by_id(self, id: str) -> bool():
        try:
            self.users = UserModel.query.filter_by(id=id).first()
            data_base.session.delete(self.users)
            data_base.session.commit()
            return True
        except Error:
            return False

    def delete_user_by_name(self, username: str) -> bool():
        try:
            self.users = UserModel.query.filter_by(username=username).first()
            data_base.session.delete(self.users)
            data_base.session.commit()
            return True
        except Error:
            return False
