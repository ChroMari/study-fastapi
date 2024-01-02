from fastapi import FastAPI
from models import User, UserMessage
from data import external_data

app = FastAPI()


@app.get("/")
async def root():
    return {"start": "Приложение успешно работает."}


@app.get("/custom")
async def read_custom_message():
    return {"start": "Кастомная страница, успешно работает."}


user = User(**external_data) # имитируем распаковку входящих данных в коде приложения
print(user)
print(user.id)

my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

@app.post("/")
async def root(user: UserMessage):
    print(f'Мы получили от юзера {user.username} такое сообщение: {user.message}')
    return user 
