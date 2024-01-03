from fastapi import FastAPI

app = FastAPI()

fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, {"username": "katya", "user_info": "любит петь"}]


@app.get("/users")  # получаем данные с сервера
async def get_all_users():
    return fake_db


@app.post("/add_user")  # отправляем информацию на сервер
async def add_user(username: str, user_info: str):
    fake_db.append({"username": username, "user_info": user_info})
    
    return {"message": "юзер успешно добавлен в базу данных"}
