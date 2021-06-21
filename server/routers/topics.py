import logging

from fastapi import APIRouter, Depends

from db.user_topics import BaseUserTopicsDB
from .users import get_current_user
from ..dependencies import get_user_topics_db
from ..models import UserModel

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/frequent')
async def frequent_topic(current_user: UserModel = Depends(get_current_user),
                         user_topics_db: BaseUserTopicsDB = Depends(get_user_topics_db)):
    user_topics = user_topics_db.get_user_topics(current_user.user_id)
    topic = user_topics.most_frequent()

    return {'topic': topic}
