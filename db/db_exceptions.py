from typing import Optional


class BaseUsersDBException(Exception):
    pass


class UserAlreadyExistsException(BaseUsersDBException):
    def __init__(self, message: str, user_id: Optional[int] = None, username: Optional[str] = None):
        self.user_id = user_id
        self.username = username
        super().__init__(message)


class UserNotExistingException(BaseUsersDBException):
    def __init__(self, message: str, user_id: Optional[int] = None, username: Optional[str] = None):
        self.user_id = user_id
        self.username = username
        super().__init__(message)
