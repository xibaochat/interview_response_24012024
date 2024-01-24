import os
import uuid
from functools import lru_cache

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import pandas as pd

from utils import init_db


router = APIRouter()


@lru_cache()
def fetch_data() -> pd.DataFrame:
    """
        Utilisation of functools.lru_cache decorator in Python helps avoid redundant data
        reading from db. It only triggers the database query only when new data is
        inserted into the database.
        :return (DataFrame): fetched data as a pandas dataframe
    """
    db = init_db()
    query = 'SELECT instruction, result FROM instruction_record;'
    data = pd.read_sql_query(query, db.connection())
    return pd.DataFrame(data)


def get_data_directory() -> str:
    """
        Create a uniq directory where the current database data version will be stored
        :return (str): created directory
    """
    unique_id = str(uuid.uuid4())
    directory_path = f'./csv/{unique_id}/'
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_data_filepath() -> str:
    """
        Return a unique filepath
        :return (str): uniquely generated filepath
    """
    directory_path = get_data_directory()
    return f'{directory_path}data.csv'


@router.get("/download_data")
def get_data_in_csv_file():
    df = fetch_data()
    file_path = get_data_filepath()
    df.to_csv(file_path, index=False)
    return FileResponse(
        file_path,
        filename='data.csv'
    )
