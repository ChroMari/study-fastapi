from .models.UserCreate import UserCreate
from fastapi import FastAPI

app = FastAPI()

@app.post("/create_user")
async def create_user(user: UserCreate) -> UserCreate:
    return user
