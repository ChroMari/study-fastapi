from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
	id: int
	name: str = "John Doe"
	signup_ts: datetime | None = None
	friends: list[int] = []

class UserMessage(BaseModel):
	username: str
	message: str

class UserId(BaseModel):
	name: str
	id: int

class UserAge(BaseModel):
	name: str
	age: int
	