import logging


from fastapi import APIRouter, Depends, Response, UploadFile
from fastapi.security import OAuth2PasswordBearer

from db.user_topics import BaseUserTopicsDB, SQLUserTopicsDB
from recognition import recognize_words
from topic import map_words
from .users import get_current_user
from ..models import UserModel

_logger = logging.getLogger(__name__)

router = APIRouter()
db: BaseUserTopicsDB = SQLUserTopicsDB()
router.db = db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


@router.post('/')
async def upload_record(recording: UploadFile, current_user: UserModel = Depends(get_current_user)):
    words = recognize_words(recording)
    topic_mapping = map_words(words)

    user_topics = router.db.get_user_topics(current_user.user_id)
    user_topics.increase_counters(topic_mapping)
    router.db.update_user_topics(user_topics)

    return Response()
