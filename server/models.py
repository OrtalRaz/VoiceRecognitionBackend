from pydantic import BaseModel

from db.users import User


class CreateUserModel(BaseModel):
    username: str
    password: str
    email: str


class UserModel(BaseModel):
    user_id: int
    username: str
    email: str

    @classmethod
    def from_user(cls, user: User):
        return cls(
            user_id=user.user_id,
            username=user.username,
            email=user.email,
        )
