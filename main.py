from fastapi import FastAPI
from pydantic import EmailStr, BaseModel #importing with pydantic, it's connected to FastAPI

from users.views import router as users_router
from items_views import router as items_router 

import uvicorn

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

@app.get("/")
def hello_index():
	return {
		"message": "Hello World",
	}


if __name__ == '__main__':
	uvicorn.run("main:app", reload=True)
