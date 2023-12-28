from .models.models import User
from .models.user import User_info

from fastapi import FastAPI

my_user_test = User(name="John Doe", id=1)
app = FastAPI()


@app.get("/users")
async def user():
    return my_user_test

@app.post("/user")
async def is_user_adult(user: User_info):
    return {"name": user.name, "age": user.age, "is_adult": user.age >= 18}
