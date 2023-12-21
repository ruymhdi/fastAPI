from fastapi import APIRouter

from users import crud
from users.schemas import CreateUser

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user: CreateUser): #EmailStr to validate (emails)
	return crud.CreateUser(user_in=user)
