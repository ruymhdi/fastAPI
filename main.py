from fastapi import FastAPI 
from pydantic import EmailStr, BaseModel #importing with pydantic, it's connected to FastAPI
import uvicorn

app = FastAPI()

class CreateUser(BaseModel):
	email: EmailStr	

@app.get("/")
def hello_index():
	return {
		"message": "Hello World",
	}

@app.get("/items/")
def list_items():
	return [
		"items1",
		"items2",
	]

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
	return {
		"item": {
			"id": item_id,
		},
	}

@app.post("/users/")
def create_user(user: CreateUser): #EmailStr to validate (emails)
	return {
		"message": "success",
		"email": user.email,
	}

@app.get("/items/latest/")
def get_lates_item():
	return {"item": {"id": "0", "name": "latest"}}


if __name__ == '__main__':
	uvicorn.run("main:app", reload=True)
