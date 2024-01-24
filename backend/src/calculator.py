from typing import Union, List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session

from models import InstructionRecord, Base

from calculator_algo import calculator

router = APIRouter()


class InstructionSchema(BaseModel):
    instruction: List[Union[str, int]]


def init_db():
    DATABASE_URL = 'postgresql://root:root@container-postgres:5432/db'
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if not 'instruction_record' in metadata.tables:
        Base.metadata.create_all(bind=engine)
    session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session_maker()


def register_to_db(instruction: List[Union[str, int]], result: int) -> bool:
    db = init_db()
    db_record = InstructionRecord(
        instruction=instruction,
        result=result
    )
    db.add(db_record)
    db.commit()
    db.close()


def instruction_exist(instruction: List[Union[str, int]]) -> bool:
    db = init_db()
    exists_query = db.query(InstructionRecord) \
                     .filter(InstructionRecord.instruction==instruction) \
                     .exists()
    return db.query(exists_query).scalar()


def fetch_instruction_result(instruction: List[Union[str, int]]) -> int:
    db = init_db()
    query = db.query(InstructionRecord) \
              .with_entities(InstructionRecord.result) \
              .filter(InstructionRecord.instruction==instruction)
    res = db.execute(query)
    db.close()
    return res.one().result


@router.post("/calculator")
def polonais_calculator(inputs: InstructionSchema) -> int:
    print('user_input:', inputs.instruction)
    if instruction_exist(inputs.instruction):
        return fetch_instruction_result(inputs.instruction)
    # Need to do calculation
    result = calculator(inputs.instruction)
    register_to_db(inputs.instruction, result)
    return result
