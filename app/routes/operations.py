from fastapi import APIRouter, Query
from app.models.operations import NumbersInput

router = APIRouter()

@router.post("/add")
def add_numbers(numbers: NumbersInput):
    result = numbers.num1 + numbers.num2
    return {"operation": "addition", "result": result}

@router.post("/multiply")
def multiply_numbers(numbers: NumbersInput):
    result = numbers.num1 * numbers.num2
    return {"operation": "multiplication", "result": result}

@router.get("/check-even-odd")
def check_even_odd(number: int = Query(..., description="Number to check")):
    result = "even" if number % 2 == 0 else "odd"
    return {"number": number, "result": result}
