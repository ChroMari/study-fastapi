from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, PositiveInt

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: EmailStr | None = Field(default=None)
    age: PositiveInt | None = Field(default=None)
    is_subscribed: bool | None


@app.post("/create_user")
async def create_user(user_create: UserCreate):
    return user_create
