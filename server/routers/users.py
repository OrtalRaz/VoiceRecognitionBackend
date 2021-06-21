import logging
import hashlib

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from db.user_topics import BaseUserTopicsDB
from server.dependencies import get_users_db, get_user_topics_db
from server.models import UserModel, CreateUserModel
from db.users import BaseUsersDB
from db.db_exceptions import UserAlreadyExistsException, UserNotExistingException

_logger = logging.getLogger(__name__)

router = APIRouter()

@router.post('/')
async def create_user(user: CreateUserModel,
                      users_db: BaseUsersDB = Depends(get_users_db),
                      user_topics_db: BaseUserTopicsDB = Depends(get_user_topics_db)) -> UserModel:
    try:
        user_id = users_db.create_user(user.username, user.password, user.email)
        new_user = users_db.get_user(user_id)
        user_topics_db.initialize_topics(user_id)
        return UserModel.from_user(new_user)
    except UserAlreadyExistsException as e:
        _logger.exception("User already exists")
        raise HTTPException(status_code=409, detail="User already exists") from e
    except Exception as e:
        _logger.exception("Failed creating user")
        raise HTTPException(status_code=500) from e


@router.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), users_db: BaseUsersDB = Depends(get_users_db)):
    if not users_db.user_exists(username=form_data.username, password=form_data.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": form_data.username, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


async def get_current_user(token: str = Depends(oauth2_scheme),
                           users_db: BaseUsersDB = Depends(get_users_db)) -> UserModel:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    username = token
    if not username:
        raise credentials_exception

    try:
        user = users_db.get_user(username)
    except UserNotExistingException as e:
        raise credentials_exception from e

    return UserModel.from_user(user)


"""
async def hash_password(form_data: OAuth2PasswordRequestForm = Depends(), password: str) -> UserModel:
    hash_object = hashlib.sha1(password)
    hex = hash_object.hexdigest()
"""