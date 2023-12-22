from sqlalchemy.ext.asyncio import create_async_engine 

from core.config import settings

class DatabaseHelper:
	def __init__(self):
		self.engine = create_async_engine(
			url=settings.db_url,
		)
