from fastapi import FastAPI

app = FastAPI()


@app.post("/calculate")
async def calculate(num1: int, num2: int):
    result = num1 + num2

    return {"результат сложения": result}
