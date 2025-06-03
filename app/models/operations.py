from pydantic import BaseModel

class NumbersInput(BaseModel):
    num1: float
    num2: float
