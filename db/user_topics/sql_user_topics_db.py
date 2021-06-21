import logging
import sqlite3

from db.db_exceptions import UserNotExistingException, UserAlreadyExistsException
from db.user_topics.base_user_topics_db import BaseUserTopicsDB, UserTopics

_logger = logging.getLogger()


class SQLUserTopicsDB(BaseUserTopicsDB):
    TABLE_NAME = 'user_topics'
    USER_ID_COLUMN = 'user_id'
    MUSIC_COLUMN = 'music'
    SPORTS_COLUMN = 'sports'
    POLITICS_COLUMN = 'politics'
    CORONA_COLUMNS = 'corona'
    FOOD_COLUMN = 'food'
    TRAVEL_COLUMN = 'travel'

    def __init__(self, db_file: str = 'users.db'):
        self._db_file = db_file

        conn = sqlite3.connect(self._db_file)
        print('connect success')

        query = f"CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} ( " \
                f"{self.USER_ID_COLUMN} INTEGER PRIMARY KEY UNIQUE, " \
                f"{self.MUSIC_COLUMN} INTEGER DEFAULT 0, " \
                f"{self.SPORTS_COLUMN} INTEGER DEFAULT 0, " \
                f"{self.POLITICS_COLUMN} INTEGER DEFAULT 0, " \
                f"{self.CORONA_COLUMNS} INTEGER DEFAULT 0, " \
                f"{self.FOOD_COLUMN} INTEGER DEFAULT 0, " \
                f"{self.TRAVEL_COLUMN} INTEGER DEFAULT 0 " \
                f")"

        conn.execute(query)
        print('create success')
        conn.commit()
        conn.close()

    def initialize_topics(self, user_id: int):
        conn = sqlite3.connect(self._db_file)
        query = f"INSERT INTO {self.TABLE_NAME} ({self.USER_ID_COLUMN}) VALUES (?)"
        with conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query, (user_id,))
            except sqlite3.IntegrityError as e:
                raise UserAlreadyExistsException(f"User topics already exist for ID {user_id}", user_id=user_id) from e
        conn.close()

        _logger.info(f"Successfully created user topics for user ID '{user_id}'")
        return user_id

    def get_user_topics(self, user_id: int) -> UserTopics:
        conn = sqlite3.connect(self._db_file)
        query = f"SELECT * FROM {self.TABLE_NAME} WHERE {self.USER_ID_COLUMN}=?"
        with conn:
            cursor = conn.execute(query, (user_id,))
            data = cursor.fetchone()
        conn.close()

        if not data:
            raise UserNotExistingException(f"No user topics for ID {user_id}", user_id=user_id)

        return UserTopics(*data)

    def update_user_topics(self, user_topics: UserTopics):
        conn = sqlite3.connect(self._db_file)
        query = f'UPDATE {self.TABLE_NAME} SET ' \
                f'{self.MUSIC_COLUMN}=?, ' \
                f'{self.SPORTS_COLUMN}=?, ' \
                f'{self.POLITICS_COLUMN}=?, ' \
                f'{self.CORONA_COLUMNS}=?, ' \
                f'{self.FOOD_COLUMN}=?, ' \
                f'{self.TRAVEL_COLUMN}=? ' \
                f'WHERE {self.USER_ID_COLUMN}=?'

        conn.execute(query, (
            user_topics.music,
            user_topics.sports,
            user_topics.politics,
            user_topics.corona,
            user_topics.food,
            user_topics.travel,
            user_topics.user_id))
        conn.commit()
        conn.close()
        print('updated success')
