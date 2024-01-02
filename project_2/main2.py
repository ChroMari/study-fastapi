from fastapi import FastAPI
from models import UserId, UserAge
from data import user_id_data

app = FastAPI()


@app.get("/users")
async def user_id():
    user: UserId = UserId(**user_id_data)

    return user


@app.post("/user")
async def write_is_adult(user: UserAge):
    user = dict(user)
    user["is_adult"] = user["age"] >= 18

    return user
