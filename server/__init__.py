from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from db.user_topics import BaseUserTopicsDB, SQLUserTopicsDB
from db.users import BaseUsersDB, SQLUsersDB
from .routers.recordings import router as recordings_router
from .routers.users import router as users_router
from .routers.topics import router as topics_router


def create_app():
    app = FastAPI()

    api_router = APIRouter()
    users_db: BaseUsersDB = SQLUsersDB()
    app.state.users_db = users_db

    user_topics_db: BaseUserTopicsDB = SQLUserTopicsDB()
    app.state.user_topics_db = user_topics_db

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

    api_router.include_router(users_router, prefix='/users')
    api_router.include_router(recordings_router, prefix='/recordings')
    api_router.include_router(topics_router, prefix='/topics')
    app.include_router(api_router, prefix='/api')

    return app
