from typing import Union, List

from utils import init_db
from models import InstructionRecord


def register_to_db(instruction: List[Union[str, int]], result: int) -> bool:
    """
    BOID
    """
    db = init_db()
    db_record = InstructionRecord(
        instruction=instruction,
        result=result
    )
    db.add(db_record)
    db.commit()
    db.close()


def instruction_exist(instruction: List[Union[str, int]]) -> bool:
    """
    BOID
    """
    db = init_db()
    exists_query = db.query(InstructionRecord) \
                     .filter(InstructionRecord.instruction==instruction) \
                     .exists()
    return db.query(exists_query).scalar()


def fetch_instruction_result(instruction: List[Union[str, int]]) -> int:
    """
    BOID
    """
    db = init_db()
    query = db.query(InstructionRecord) \
              .with_entities(InstructionRecord.result) \
              .filter(InstructionRecord.instruction==instruction)
    res = db.execute(query)
    db.close()
    return res.one().result
