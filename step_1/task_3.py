from fastapi import FastAPI
from pydantic import BaseModel

class Number(BaseModel):
    num1: int
    num2: int

app = FastAPI()


@app.post("/calculate")
async def calculate(number: Number):
    result_summ = number.num1 + number.num2

    return {"result": result_summ}
