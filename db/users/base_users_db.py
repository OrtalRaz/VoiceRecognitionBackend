from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import overload


@dataclass
class User:
    user_id: int
    username: str
    password: str
    email: str


class BaseUsersDB(metaclass=ABCMeta):
    @overload
    def get_user(self, user_id: int) -> User:
        ...

    @overload
    def get_user(self, username: str) -> User:
        ...

    @abstractmethod
    def get_user(self, identifier) -> User:
        """
        :param identifier: An identifier (ID/name) of the user to get.
        :return: User with given ID.
        :raises UserNotExistingException: If no user with such ID exists.
        """
        pass

    @abstractmethod
    def create_user(self, username: str, password: str, email: str) -> int:
        """
        Insert a new user to the DB.
        :param username: The new username.
        :param password: New user's password.
        :param email: New user's email.
        :return: New user's ID.
        :raises UserAlreadyExistsException: In case a user with such name already exists.
        """

    @abstractmethod
    def delete_user(self, user_id: int):
        pass

    @abstractmethod
    def update_username(self, user_id: int, new_name: str):
        pass

    @abstractmethod
    def update_password(self, user_id: int, new_password: str):
        pass

    @abstractmethod
    def user_exists(self, username: str, password: str) -> bool:
        pass
