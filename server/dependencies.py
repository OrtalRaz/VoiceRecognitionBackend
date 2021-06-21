from fastapi import Request

from db.user_topics import BaseUserTopicsDB
from db.users import BaseUsersDB


def get_users_db(request: Request) -> BaseUsersDB:
    return request.app.state.users_db


def get_user_topics_db(request: Request) -> BaseUserTopicsDB:
    return request.app.state.user_topics_db
