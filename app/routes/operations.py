from fastapi import APIRouter, Depends
from app.models.operations import NumbersInput
from app.auth import get_current_active_user

router = APIRouter()

@router.post("/add")
def add_numbers(numbers: NumbersInput, user=Depends(get_current_active_user)):
    result = numbers.num1 + numbers.num2
    return {"operation": "addition", "user": user["username"], "result": result}

@router.post("/multiply")
def multiply_numbers(numbers: NumbersInput, user=Depends(get_current_active_user)):
    result = numbers.num1 * numbers.num2
    return {"operation": "multiplication", "user": user["username"], "result": result}

@router.get("/check-even-odd")
def check_even_odd(number: int, user=Depends(get_current_active_user)):
    result = "even" if number % 2 == 0 else "odd"
    return {"number": number, "result": result, "checked_by": user["username"]}
