from fastapi import FastAPI
from pydantic import BaseModel

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

class Product(BaseModel):
    product_id: int
    name: str
    category: str
    price: float

sample_products: list[Product] = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

app = FastAPI()

@app.get("/product/{product_id}")
async def information_of_product(product_id: int) -> Product | dict: #`product_id`: идентификатор продукта (целое число)
    if (product_id - 1) in range(len(sample_products)):
        return sample_products[product_id - 1]
    else:
        return {"error": "Такого продукта у нас нету."}


# `keyword` (строка, обязательна): ключевое слово для поиска товаров.
# `category` (строка, необязательно): категория для фильтрации товаров.
# `limit` (целое число, необязательно): максимальное количество товаров для возврата (по умолчанию 10, если не указано иное).
@app.get("/products/search")
async def search_product(keyword: str, category: str = "", limit: int = 10) -> list[Product]: 
    products = []

    for product in sample_products:
        if keyword.lower() in product['name'].lower() and category.lower() in product['category'].lower():
            products.append(product)

    return products[:limit]
