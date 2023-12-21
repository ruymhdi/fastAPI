from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from annotated_types import MinLen, MaxLen

class CreateUser(BaseModel):
	# username: str = Field(..., min_length=3, max_length=20) #using only anoneted Min and Max
	username: Annotated[str, MinLen(3), MaxLen(20)]
	email: EmailStr	