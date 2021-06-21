import logging


from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from db.user_topics import BaseUserTopicsDB, SQLUserTopicsDB
from .users import get_current_user
from ..models import UserModel

_logger = logging.getLogger(__name__)

router = APIRouter()
db: BaseUserTopicsDB = SQLUserTopicsDB()
router.db = db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


@router.get('/frequent')
async def frequent_topic(current_user: UserModel = Depends(get_current_user)):
    user_topics = router.db.get_user_topics(current_user.user_id)
    topic = user_topics.most_frequent()

    return {'topic': topic}
