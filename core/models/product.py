from .base import Base
from sqlalchemy.orm import Mapped


class Product(Base):
	__tablename__ = True

	name: Mapped[str]
	description: Mapped[str]
	price: Mapped[int]
