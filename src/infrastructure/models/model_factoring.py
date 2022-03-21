from abc import ABC

from src.infrastructure.adapters.sqlite3_adapter import Sqlite3Adapter
from src.infrastructure.exceptions.insert_exception import InsertException


class ModelFactoring(ABC):
    def __init__(self):
        self.table_name: str = ""
        self.connect = Sqlite3Adapter().connect()

    def table(self, args: list):
        cursor = self.connect.cursor()
        query: list = list()
        query.append("CREATE TABLE IF NOT EXISTS {} (".format(self.table_name))
        query.append(', '.join(args))
        query.append(");")
        cursor.execute(''.join(query))
        cursor.close()

    def show(self, where: list, values: list) -> list:
        cursor = self.connect.cursor()
        query: list = list()
        query.append("SELECT * FROM {} WHERE ".format(self.table_name))
        count = 0
        for row in where:
            count += 1
            if count == len(where):
                query.append('"{}" = "{}" ;'.format(row, values[count - 1]))
            else:
                query.append('"{}" = "{}", '.format(row, values[count - 1]))
        cursor.execute(''.join(query))
        result = cursor.fetchall()
        cursor.close()
        return result

    def list(self) -> list:
        cursor = self.connect.cursor()
        query: list = list()
        query.append('SELECT * FROM "{}";'.format(self.table_name))
        cursor.execute(''.join(query))
        result = cursor.fetchall()
        cursor.close()
        return result

    def select(self, fields: list, where: list, values: list) -> list:
        cursor = self.connect.cursor()
        query: list = list()
        query.append('SELECT ')
        count = 0
        for row in fields:
            count += 1
            if count == len(fields):
                query.append('"{}" '.format(row))
            else:
                query.append('"{}", '.format(row))
        query.append("FROM {} WHERE ".format(self.table_name))
        count = 0
        for row in where:
            count += 1
            if count == len(where):
                query.append('"{}" = "{}" ;'.format(row, values[count - 1]))
            else:
                query.append('"{}" = "{}", '.format(row, values[count - 1]))
        cursor.execute(''.join(query))
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert(self, fields: list, inserts: list) -> bool():
        try:
            cursor = self.connect.cursor()
            query: list = list()
            query.append('INSERT INTO "{}" ('.format(self.table_name))
            count = 0
            for row in fields:
                count += 1
                if count == len(fields):
                    query.append('"{}") '.format(row))
                else:
                    query.append('"{}", '.format(row))
            query.append('VALUES (')
            count = 0
            for row in inserts:
                count += 1
                if count == len(inserts):
                    query.append('"{}");'.format(row))
                else:
                    query.append('"{}", '.format(row))
            cursor.execute("".join(query))
            self.connect.commit()
            result = cursor.rowcount
            cursor.close()
            return result
        except Exception:
            raise InsertException(self.table_name)

    def update(self, fields: list, inserts: list, where: list, values: list):
        cursor = self.connect.cursor()
        query: list = list()
        query.append("UPDATE {} SET ".format(self.table_name))
        count = 0
        for row in fields:
            count += 1
            if count == len(fields):
                query.append('"{} = {} ") '.format(row, inserts[count - 1]))
            else:
                query.append('"{} = {}, ", '.format(row, inserts[count - 1]))
        query.append('WHERE ')
        count = 0
        for row in where:
            count += 1
            if count == len(where):
                query.append('"{}" = "{}" ;'.format(row, values[count - 1]))
            else:
                query.append('"{}" = "{}", '.format(row, values[count - 1]))
        cursor.execute(''.join(query))
        result = cursor.fetchall()
        cursor.close()
        return result

    def delete(self, where: list, values: list) -> bool():
        cursor = self.connect.cursor()
        query: list = list()
        query.append('DELETE FROM {} WHERE '.format(self.table_name))
        count = 0
        for row in where:
            count += 1
            if count == len(where):
                query.append('"{}" = "{}" ;'.format(row, values[count - 1]))
            else:
                query.append('"{}" = "{}", '.format(row, values[count - 1]))
        cursor.execute("".join(query))
        self.connect.commit()
        result = cursor.lastrowid
        cursor.close()
        return result
