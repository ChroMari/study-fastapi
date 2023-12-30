from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    try:
        # тут добавили дополнительную проверку
        if item.price < 0:
            raise ValueError("Price must be non-negative")
        
        # это вернётся в случае успеха
        return {"message": "Item created successfully", "item": item}
    except ValueError as ve:
        # обрабатываем нашу ошибку валидации и пробрасываем ошибку выше с кастомным ответом
        raise HTTPException(status_code=400, detail=str(ve))