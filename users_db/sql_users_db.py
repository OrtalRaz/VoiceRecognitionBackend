import sqlite3

from .base_users_db import BaseUsersDB, User
from .db_exceptions import UserNotExistingException


class SQLUsersDB(BaseUsersDB):
    TABLE_NAME = 'users'
    USER_ID_COLUMN = 'user_id'
    USERNAME_COLUMN = 'username'
    PASSWORD_COLUMN = 'password'
    EMAIL_COLUMN = 'email'


    def __init__(self, db_file: str = 'users.db'):
        self._db_file = db_file

        conn = sqlite3.connect(self._db_file)
        print('connect success')

        query = f"CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} ( " \
                f"{self.USER_ID_COLUMN} INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                f"{self.USERNAME_COLUMN} TEXT NOT NULL UNIQUE, " \
                f"{self.PASSWORD_COLUMN} TEXT NOT NULL, " \
                f"{self.EMAIL_COLUMN} TEXT NOT NULL UNIQUE" \
                f")"

        conn.execute(query)
        print('create success')
        conn.commit()
        conn.close()


    def __str__(self):
        return 'TABLE: ', self.TABLE_NAME

    def get_user(self, user_id: int) -> User:
        conn = sqlite3.connect(self._db_file)
        query = f"SELECT * FROM {self.TABLE_NAME} WHERE {self.USER_ID_COLUMN}=?"
        with conn:
            cursor = conn.execute(query, (user_id,))
            data = cursor.fetchone()
        conn.close()

        if not data:
            raise UserNotExistingException(f"No user with ID {user_id}", user_id=user_id)

        return User(*data)

    def insert_user(self, username: str, password: str, email: str) -> int:
        conn = sqlite3.connect(self._db_file)
        query = f"INSERT INTO {self.TABLE_NAME} (" \
                f"{self.USERNAME_COLUMN},{self.PASSWORD_COLUMN},{self.EMAIL_COLUMN}) VALUES (?,?,?)"
        with conn:
            cursor = conn.cursor()
            cursor.execute(query, (username, password, email))
            user_id = cursor.lastrowid
        conn.close()

        print('insert success')
        return user_id


    def delete_user(self, user_id: int):
        conn = sqlite3.connect(self._db_file)
        query = f'DELETE FROM {self.TABLE_NAME} WHERE {self.USER_ID_COLUMN}=?'

        print('delete' + query)
        conn.execute(query, (user_id,))
        conn.commit()
        conn.close()
        print('delete success')

    def update_username(self, user_id: int, new_name: str):
        conn = sqlite3.connect(self._db_file)
        query = f'UPDATE {self.TABLE_NAME} SET {self.USERNAME_COLUMN}=?  WHERE {self.USER_ID_COLUMN}=?'

        print('update' + query)
        conn.execute(query, (new_name, user_id))
        conn.commit()
        conn.close()
        print('updated success')


    def update_password(self, user_id: int, new_password: str):
        conn = sqlite3.connect(self._db_file)
        query = f'UPDATE {self.TABLE_NAME} SET {self.PASSWORD_COLUMN}=? WHERE {self.USER_ID_COLUMN}=?'

        print('update' + query)
        conn.execute(query, (new_password, user_id))
        conn.commit()
        conn.close()
        print('updated success')

    def user_exists(self, username: str, password: str) -> bool:
        try:
            conn = sqlite3.connect(self._db_file)
            print('open success')
            txt = f"SELECT * FROM {self.TABLE_NAME}" \
                  f"WHERE {self.USERNAME_COLUMN}={username} AND {self.PASSWORD_COLUMN}={password};"
            cursor = conn.execute(txt)
            print("Operation done successfully")
            return bool(cursor.rowcount)
        except:
            return False
