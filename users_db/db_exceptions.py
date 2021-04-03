from typing import Optional


class BaseUsersDBException(Exception):
    pass


class UserNotExistingException(BaseUsersDBException):
    def __init__(self, message: str, user_id: Optional[int] = None):
        self.user_id = user_id
        super().__init__(message)
