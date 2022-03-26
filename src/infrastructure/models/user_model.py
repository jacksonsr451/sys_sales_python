from src.infrastructure.adapters.user_model_adapter import UserModelAdapter


class UserModel(UserModelAdapter):
    def __init__(self, data: {} = None):
        super(UserModel, self).__init__()
        if data is not None:
            self.id: str = data["id"]
            self.username: str = data["username"]
            self.email: str = data["email"]
            self.password: str = data["password"]
