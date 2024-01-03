from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    user_info: str

fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, {"username": "katya", "user_info": "любит петь"}]


@app.get("/user")
async def get_all_users():
    return fake_db


@app.post("/add_user", response_model=User)  # указали модель (формат) ответа
async def add_user(user: User):
    fake_db.append({"username": user.username, "user_info": user.user_info})
    
    return {"message": "юзер успешно добавлен в базу данных"}
