from fastapi import FastAPI

app = FastAPI()

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

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]


@app.get("/product/{product_id}")
async def get_product_id(product_id: int):
    for product in sample_products:
        if product_id == product["product_id"]:
            return product
        
    return {"status": "Нет такого продукта."}


@app.get("/products/search")
async def search_products(keyword: str, category: str = '', limit: int = 10):
    result_search = []
    for product in sample_products:
        if keyword.lower() in product["name"].lower() and category.lower() in product["category"].lower():
            result_search.append(product)

    return result_search[:limit]
