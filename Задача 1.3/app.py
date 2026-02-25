from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: int
    num2: int


@app.post("/calculate/")
async def calculate(number: Numbers):
    sum_result = number.num1 + number.num2
    return {"result": sum_result}