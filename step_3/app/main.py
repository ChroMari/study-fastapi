from fastapi import FastAPI
from pydantic import BaseModel # это обычно отдельный файл модели, приводим код единым текстом для наглядности


app = FastAPI()

@app.get('/{user_id}') # тут объявили параметр пути
async def search_user_by_id(user_id: int): # тут указали его тип данных
    # какая-то логика работы поиска
    return {"вы просили найти юзера с id": user_id}

# ---
fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, {"username": "katya", "user_info": "любит петь"}]

@app.get('/users2') # маршрут GET для ПОЛУЧЕНИЯ каких-то данных с сервера
async def get_all_users():
    return fake_db
    
@app.post('/add_user') # маршрут POST для отправления какой-то информации на сервер
async def add_user(username: str, user_info: str): # принимает два query-параметра, про которые будет рассказано дальше в этом уроке (это не типичный пример пост-запроса)
    fake_db.append({"username": username, "user_info": user_info})
    return {"message": "юзер успешно добавлен в базу данных"}

# ---
class User(BaseModel): # обычно размещаются в файле models.py
    username: str
    user_info: str


# тут добавили проверку данных на основании модели        
@app.post('/add_user_new_type')
async def add_user(user: User): # собственно тут проверяем входные данные на соответствие модели
    fake_db.append({"username": user.username, "user_info": user.user_info}) # тут добавили юзера в фейковую БД
    return {"message": "юзер успешно добавлен в базу данных"}

# ---
# тут добавили проверку данных на основании модели, а также указываем модель ответа        
@app.post('/add_user_new_type_two', response_model=User) # тут указали модель (формат) ответа
async def add_user(user: User): # собственно тут проверяем входные данные на соответствие модели
    fake_db.append({"username": user.username, "user_info": user.user_info}) # тут добавили юзера в фейковую БД
    return user

#---
# Пример пользовательских данных (для демонстрационных целей) 
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

# Конечная точка для получения информации о пользователе по ID
@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}