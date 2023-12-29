from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


# --- Модели запросов и ответов.
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item: # тут мы передали в наш обработчик Pydantic модель, чтобы она проверяла все запросы на соответствие этой модели (все поля и типы данных в них должны соответствовать модели
    return item


@app.get("/items/")
async def read_items() -> list[Item]: # тут мы не принимаем никаких данных, но указываем, что возвращаться будет список, содержащий в себе Pydantic модели    
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ] 

# --- Обработка загрузки файла.
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# --- Обработка параметров запроса.
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items_db/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
