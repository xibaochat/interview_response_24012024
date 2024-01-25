from typing import Union, List

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from calculator_algo import calculator, CalculationException
from db_actions import (
    register_to_db,
    instruction_exist,
    fetch_instruction_result,
    fetch_data
)
from utils import get_data_filepath


router = APIRouter()


class CalculatorSchema(BaseModel):
    instruction: List[Union[str, float]]


@router.post(
    "/calculator",
    tags=["polish-calculator"],
    summary="Calculate given instructions using polish calculator model",
    response_description="Calculation result",
)
def polish_calculator(inputs: CalculatorSchema) -> float:
    # Skip calculation if it already exists in db
    if instruction_exist(tuple(inputs.instruction)):
        return fetch_instruction_result(tuple(inputs.instruction))

    try:
        result = calculator(inputs.instruction)
    except CalculationException:
        raise HTTPException(
            status_code=400,
            detail='Something went wrong with the provided inputs.'
        )

    register_to_db(inputs.instruction, result)
    return result


@router.get(
    "/download_data",
    tags=["download-data"],
    summary="""
    Download the existings instructions and results from the database
    """,
    response_description="""
    CSV file containing all instructions with their results
    """,
)
def get_data_in_csv_file():
    df = fetch_data()
    file_path = get_data_filepath()
    df.to_csv(file_path, index=False)
    return FileResponse(
        file_path,
        filename='data.csv'
    )
