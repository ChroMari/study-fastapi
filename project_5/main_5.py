from fastapi import FastAPI, Response, Cookie
from pydantic import BaseModel

app = FastAPI()

fake_user_bd = [
    {
        "username": "user123",
        "password": "password123",
        "session_token": None
    },
    {
        "username": "user234",
        "password": "password345",
        "session_token": None
    },
]

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
async def sing_user(user: User, response: Response):
    user = dict(user)
    for db_user in fake_user_bd:
        if user["username"] == db_user["username"] and user["password"] == db_user["password"]:
            response.set_cookie(key="session_token", value="abc123xyz456")
            db_user["session_token"] = "abc123xyz456"
    return user


@app.get("/user")
async def login(session_token: str | None = Cookie(default=None)):
    for db_user in fake_user_bd:
        if session_token == db_user["session_token"]:
            return db_user
        
    return  {"message": "Unauthorized"}
