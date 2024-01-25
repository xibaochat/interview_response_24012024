from typing import Union, List, Tuple
from functools import lru_cache
import pandas as pd

from utils import init_db
from models import InstructionRecord


def register_to_db(instruction: List[Union[str, float]], result: float):
    """
        initialize db, creates an item of table,  adds it to db, \
        commits the changes, and then closes the database connection.\
        :param (List) instruction: instruction from user
    """
    db = init_db()
    db_record = InstructionRecord(
        instruction=instruction,
        result=result
    )
    db.add(db_record)
    db.commit()
    db.close()


def instruction_exist(instruction: Tuple[Union[str, float]]) -> bool:
    """
        check if the instruction is already in db
        :param (List) instruction: instruction from user
        :return (bool): if instruction is already exist
    """
    db = init_db()
    exists_query = db.query(InstructionRecord) \
                     .filter(InstructionRecord.instruction == instruction)\
                     .exists()
    res = db.query(exists_query).scalar()
    db.close()
    return res


def fetch_instruction_result(instruction: Tuple[Union[str, float]]) -> float:
    """
    retrieve the result from a given existed instruction in db
    :return (float): fetched result of instruction
    """
    db = init_db()
    query = db.query(InstructionRecord) \
              .with_entities(InstructionRecord.result) \
              .filter(InstructionRecord.instruction == instruction)
    res = db.execute(query)
    db.close()
    return res.one().result


@lru_cache(maxsize=None)
def fetch_data(nb_to_fetch: int) -> pd.DataFrame:
    """
        Utilisation of functools.lru_cache decorator \
        in Python helps avoid redundant data
        reading from db. It only triggers the database query \
        only when new data is inserted into the database.\
        :return (DataFrame): fetched data as a pandas dataframe
    """
    db = init_db()
    query = 'SELECT instruction, result FROM instruction_record;'
    data = pd.read_sql_query(query, db.connection())
    db = init_db()
    db.close()
    return pd.DataFrame(data)


def count_nb_instructions() -> int:
    """
        Return how much instructions there currently are in the db
        :return (int): count
    """
    db = init_db()
    res = db.query(InstructionRecord).count()
    db.close()
    return res
