from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    username: str
    password: str
    email: str


class BaseUsersDB(metaclass=ABCMeta):
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        """
        :param user_id: The ID of the user to get.
        :return: User with given ID.
        :raises UserNotExistingException: If no user with such ID exists.
        """
        pass

    @abstractmethod
    def insert_user(self, username: str, password: str, email: str) -> int:
        pass

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
