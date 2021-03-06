import logging

from fastapi import APIRouter, Depends, UploadFile, File
from starlette.responses import JSONResponse

from db.user_topics import BaseUserTopicsDB
from recognition import recognize_words
from topic import map_words
from .users import get_current_user
from ..dependencies import get_user_topics_db
from ..models import UserModel

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.post('/')
async def upload_record(recording: UploadFile = File(...), current_user: UserModel = Depends(get_current_user),
                        user_topics_db: BaseUserTopicsDB = Depends(get_user_topics_db)):
    words = recognize_words(recording.file)
    topic_mapping = map_words(words)

    user_topics = user_topics_db.get_user_topics(current_user.user_id)
    user_topics.increase_counters(topic_mapping)
    user_topics_db.update_user_topics(user_topics)

    return JSONResponse()
