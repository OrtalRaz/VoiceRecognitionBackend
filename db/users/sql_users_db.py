import logging
import sqlite3

from .base_users_db import BaseUsersDB, User
from db.db_exceptions import UserAlreadyExistsException, UserNotExistingException

_logger = logging.getLogger()


class SQLUsersDB(BaseUsersDB):
    TABLE_NAME = 'users'
    USER_ID_COLUMN = 'user_id'
    USERNAME_COLUMN = 'username'
    PASSWORD_COLUMN = 'password'
    EMAIL_COLUMN = 'email'


    def __init__(self, db_file: str = 'users.db'):
        self._db_file = db_file

        conn = sqlite3.connect(self._db_file)

        query = f"CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} ( " \
                f"{self.USER_ID_COLUMN} INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                f"{self.USERNAME_COLUMN} TEXT NOT NULL UNIQUE, " \
                f"{self.PASSWORD_COLUMN} TEXT NOT NULL, " \
                f"{self.EMAIL_COLUMN} TEXT NOT NULL UNIQUE" \
                f")"

        with conn:
            conn.execute(query)

        _logger.info("Successfully initialized database")
        conn.close()


    def __str__(self):
        return 'TABLE: ', self.TABLE_NAME

    def get_user(self, identifier) -> User:
        conn = sqlite3.connect(self._db_file)

        if isinstance(identifier, int):
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE {self.USER_ID_COLUMN}=?"
        else:
            query = f"SELECT * FROM {self.TABLE_NAME} WHERE {self.USERNAME_COLUMN}=?"
        with conn:
            cursor = conn.execute(query, (identifier,))
            data = cursor.fetchone()
        conn.close()

        if not data:
            if isinstance(identifier, int):
                raise UserNotExistingException(f"No user with ID {identifier}", user_id=identifier)
            else:
                raise UserNotExistingException(f"No user with name {identifier}", username=identifier)

        return User(*data)

    def create_user(self, username: str, password: str, email: str) -> int:
        conn = sqlite3.connect(self._db_file)
        query = f"INSERT INTO {self.TABLE_NAME} (" \
                f"{self.USERNAME_COLUMN},{self.PASSWORD_COLUMN},{self.EMAIL_COLUMN}) VALUES (?,?,?)"
        with conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query, (username, password, email))
            except sqlite3.IntegrityError as e:
                raise UserAlreadyExistsException("User already exists", username=username) from e
            user_id = cursor.lastrowid
        conn.close()

        _logger.info(f"Successfully created user '{username}'")
        return user_id


    def delete_user(self, user_id: int):
        conn = sqlite3.connect(self._db_file)
        query = f'DELETE FROM {self.TABLE_NAME} WHERE {self.USER_ID_COLUMN}=?'

        with conn:
            conn.execute(query, (user_id,))
        conn.close()
        _logger.info(f"Successfully deleted user ID {user_id}")

    def update_username(self, user_id: int, new_name: str):
        conn = sqlite3.connect(self._db_file)
        query = f'UPDATE {self.TABLE_NAME} SET {self.USERNAME_COLUMN}=?  WHERE {self.USER_ID_COLUMN}=?'

        with conn:
            conn.execute(query, (new_name, user_id))
        conn.close()
        _logger.info(f"Updated username of user ID {user_id} to '{new_name}'")


    def update_password(self, user_id: int, new_password: str):
        conn = sqlite3.connect(self._db_file)
        query = f'UPDATE {self.TABLE_NAME} SET {self.PASSWORD_COLUMN}=? WHERE {self.USER_ID_COLUMN}=?'

        with conn:
            conn.execute(query, (new_password, user_id))
        conn.close()
        _logger.info(f"Successfully updated password of user ID {user_id}")

    def user_exists(self, username: str, password: str) -> bool:
        try:
            conn = sqlite3.connect(self._db_file)
            query = f"SELECT * FROM {self.TABLE_NAME} " \
                    f"WHERE {self.USERNAME_COLUMN}=? AND {self.PASSWORD_COLUMN}=?;"
            cursor = conn.execute(query, (username, password))
            return bool(cursor.rowcount)
        except Exception:
            return False


    def get_password(self, password: str) -> str:
        pass
