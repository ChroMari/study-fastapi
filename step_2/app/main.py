from fastapi import FastAPI

app = FastAPI()

# пример роута (маршрута)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}
