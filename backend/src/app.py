from typing import List, Union

from fastapi import FastAPI, Query, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from health import router as health_router
from calculator import router as calculator_router
from csv_file import router as csv_file_router

app = FastAPI()

origins = ['*']


app.include_router(health_router)
app.include_router(calculator_router)
app.include_router(csv_file_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
