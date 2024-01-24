from typing import Union, List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from calculator_algo import calculator, CalculationException
from db_actions import (
    register_to_db,
    instruction_exist,
    fetch_instruction_result
)


router = APIRouter()


class InstructionSchema(BaseModel):
    instruction: List[Union[str, int]]


@router.post(
    "/calculator",
    tags=["polish-calculator"],
    summary="Calculate given instructions using polish calculator model",
    response_description="Calculation result",
)
def polonais_calculator(inputs: InstructionSchema) -> int:
    """
        Make polish calculation.
    """
    # Skip calculation if it already exists in db
    if instruction_exist(inputs.instruction):
        return fetch_instruction_result(inputs.instruction)

    try:
        result = calculator(inputs.instruction)
    except (ValueError, CalculationException):
        raise HTTPException(
            status_code=400,
            detail='Something went wrong with the provided inputs.'
        )

    register_to_db(inputs.instruction, result)
    return result
