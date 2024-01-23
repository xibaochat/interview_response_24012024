from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()
origins = ['*']

class UserInput(BaseModel):
    user_input: List

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class MissingEnvVar(Exception):
    pass

@app.get("/")
async def home_page():
     return {"greeting":"Hello world"}



def change_datatype(user_input: List[str]):
    for i in range(len(user_input)):
        if '.' in  user_input[i] and user_input[i].replace(".", "").isnumeric():
            user_input[i] = float(user_input[i])
        elif user_input[i] .isnumeric():
            user_input[i]  = int(user_input[i] )
    return user_input

@app.post("/")
async def polonais_calculator(user_input: List[str], alias="user_input") -> int:
    print('user_input:', user_input)
    user_input = change_datatype(user_input)
    print(f'after user_input{user_input}')
    arr = []
    for i in user_input:
        if isinstance(i, int) or isinstance(i, float):
            arr.append(i)
        elif (isinstance(i, str)):
            b, a = arr.pop(), arr.pop()
            expr = f"{a} {i} {b}"
            arr.append(eval(expr))
        else:
            raise ValueError(f"Expression invalide: {touche}")
    if len(arr) != 1:
        _msg = 'Invalid input'
        raise MissingEnvVar(_msg) from None
    res = arr.pop()
    return res
