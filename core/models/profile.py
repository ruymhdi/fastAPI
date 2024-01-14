from .base import Base
from .mixins import UserRelationMixin

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .user import User


class Profile(UserRelationMixin, Base):
	_user_id_unique = True
	_user_back_populates = "profile"
	first_name: Mapped[str | None] = mapped_column(String(40), unique=False)
	last_name: Mapped[str | None] = mapped_column(String(40), unique=False)
	bio: Mapped[str | None]