from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class InstructionRecord(Base):
    __tablename__ = 'instruction_record'
    id  = Column(Integer, primary_key=True, index=True)
    instruction = Column(ARRAY(String), nullable=False, unique=True)
    result = Column(Integer, nullable=True)
