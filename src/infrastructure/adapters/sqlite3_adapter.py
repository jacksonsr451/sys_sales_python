import os
import sqlite3

from src.infrastructure.adapters.connect_db_interface import ConnectDBInterface


class Sqlite3Adapter(ConnectDBInterface):
    def __init__(self):
        self.sqlite = sqlite3
        self.path_database: str = self.set_path_database()

    def connect(self):
        return self.sqlite.connect(self.path_database)

    @classmethod
    def set_path_database(cls):
        path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(path, '../../../data/data.sqlite')
