from .base import Base

class Product(Base):
	__tablename__ = True

	name: Mapped[str]
	description: Mapped[str]
	price: Mapped[int]
	