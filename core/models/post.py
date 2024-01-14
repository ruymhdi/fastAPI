from .base import Base
from .mixins import UserRelationMixin

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text


class Post(UserRelationMixin,Base):
    # _user_id_nullable = False
    # _user_id_unique = False
    _user_back_populates = "posts"

    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
	    Text, 
		default="",
		server_default="",
    )
