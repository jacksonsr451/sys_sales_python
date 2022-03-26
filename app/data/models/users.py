from sqlalchemy import String, Column

from app.extensions.flask_sqlalchemy import data_base


class Users(data_base.Model):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
