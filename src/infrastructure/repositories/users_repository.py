from domain.src.gateweys.registration_gateway import RegistrationGateway
from domain.src.interfaces.registration_interface import RegistrationInterface
from src.infrastructure.adapters.database_connection_adapter import DatabaseConnectionAdapter
from src.infrastructure.adapters.user_model_adapter import UserModelAdapter
from src.infrastructure.exceptions.insert_exception import InsertException
from src.infrastructure.models.user_model import UserModel


class UsersRepository(
    RegistrationGateway
):
    def __init__(self):
        self.users: UserModelAdapter = UserModel()
        self.connection = DatabaseConnectionAdapter.get_connection()
        self.data = {"id": "", "username": "", "email": "", "password": ""}

    def insert_new_user(self, registration: RegistrationInterface) -> bool():
        try:
            self.__init_data(registration=registration)
            self.connection.session.add(UserModel(data=self.data))
            self.connection.session.commit()
            return True
        except Exception:
            self.connection.session.rollback()
            raise InsertException("users")
        finally:
            self.connection.session.close()

    def __init_data(self, registration: RegistrationInterface):
        self.data["id"] = registration.get_id()
        self.data["username"] = registration.get_username()
        self.data["email"] = registration.get_email()
        self.data["password"] = registration.get_password()

    def delete_user_by_id(self, id: str) -> bool():
        try:
            self.connection.session.delete(UserModel.find_by_id(id=id))
            self.connection.session.commit()
            return True
        except Exception:
            self.connection.session.rollback()
            raise
        finally:
            self.connection.session.close()

    def delete_user_by_username(self, username: str) -> bool():
        try:
            self.connection.session.delete(UserModel.find_by_username(username=username))
            self.connection.session.commit()
            return True
        except Exception:
            self.connection.session.rollback()
            raise
        finally:
            self.connection.session.close()
