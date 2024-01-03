from fastapi import FastAPI

app = FastAPI()


@app.get("/{user_id}")
async def search_user_by_id(user_id: int):
    return {"вы просили найти юзера с id": user_id}