import os

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
