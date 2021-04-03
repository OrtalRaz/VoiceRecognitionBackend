import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from users_db import BaseUsersDB, SQLUsersDB, User

IP = '0.0.0.0'
PORT = 1730

_logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db: BaseUsersDB = SQLUsersDB()
app.db = db


class CreateUserModel(BaseModel):
    username: str
    password: str
    email: str


class UserModel(BaseModel):
    user_id: int
    username: str
    password: str
    email: str

    @classmethod
    def from_user(cls, user: User):
        return cls(
            user_id=user.user_id,
            username=user.username,
            password=user.password,
            email=user.email,
        )


@app.get('/')
async def index():
    return {'a': 'b'}


@app.post('/users')
async def create_user(user: CreateUserModel) -> UserModel:
    try:
        user_id = app.db.insert_user(user.username, user.password, user.email)
        new_user = app.db.get_user(user_id)
        return UserModel.from_user(new_user)
    except Exception:
        _logger.exception("Failed creating user")
        raise HTTPException(status_code=500)
