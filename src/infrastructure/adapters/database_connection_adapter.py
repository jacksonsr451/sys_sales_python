from app.extensions.flask_sqlalchemy import data_base


class DatabaseConnectionAdapter:
    @classmethod
    def get_connection(cls):
        return data_base
