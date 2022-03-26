from app.extensions.flask_sqlalchemy import data_base


class UserModel(data_base.Model):
    __tablename__ = "users"
    id = data_base.Column(data_base.String(50), primary_key=True)
    username = data_base.Column(data_base.String(50), unique=True, nullable=False)
    email = data_base.Column(data_base.String(50), unique=True, nullable=False)
    password = data_base.Column(data_base.String(150), nullable=False)

    def __init__(self, data: {} = None):
        if data is not None:
            self.id: str = data["id"]
            self.username: str = data["username"]
            self.email: str = data["email"]
            self.password: str = data["password"]
