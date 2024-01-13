from fastapi import FastAPI
from pydantic import EmailStr, BaseModel #importing with pydantic, it's connected to FastAPI
from contextlib import asynccontextmanager

from core.config import settings
from api_v1 import router as router_v1
from users.views import router as users_router
from items_views import router as items_router 

import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):

	yield	

app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)

@app.get("/")
def hello_index():
	return {
		"message": "Hello World",
	}


if __name__ == '__main__':
	uvicorn.run("main:app", reload=True)
