import os
import uuid

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session

from models import Base


def init_db() -> Session:
    try:
        db_url = os.environ['DB_URL']
    except KeyError as err:
        raise ValueError('Missing environment variable DB_URL') from err

    engine = create_engine(db_url)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    session_maker = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    # Should probably be isolated somewhere else
    if 'instruction_record' not in metadata.tables:
        Base.metadata.create_all(bind=engine)

    return session_maker()


def get_data_directory() -> str:
    """
        Create a uniq directory where the current database \
        data version will be stored
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
