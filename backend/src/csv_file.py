from fastapi import APIRouter, HTTPException
import pandas as pd
from sqlalchemy import create_engine
from fastapi.responses import FileResponse
import uuid
import os
import functools


router = APIRouter()
DATABASE_URL = 'postgresql://root:root@container-postgres:5432/db'

@functools.lru_cache(maxsize=None)
def fetch_data():
    engine = create_engine(DATABASE_URL)
    query = 'SELECT instruction, result FROM instruction_record;'
    with engine.connect() as conn, conn.begin():
        data = pd.read_sql_query(query, conn)
        df = pd.DataFrame(data)
        if df.empty:
            raise RuntimeError("No item inside the table")
        return df

@router.get("/download_data")
def get_data_in_csv_file():
    try:
        df = fetch_data()
    except RuntimeError as re:
        raise HTTPException(status_code=500, detail=f"{re}")
    unique_id = str(uuid.uuid4())
    directory_path = f"./csv/{unique_id}/"
    os.makedirs(directory_path, exist_ok=True)
    file_path = f"{directory_path}data.csv"
    df.to_csv(file_path, index=False)
    return FileResponse(file_path, filename='data.csv')
