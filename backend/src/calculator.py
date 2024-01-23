from fastapi import APIRouter


router = APIRouter()

class MissingEnvVar(Exception):
    pass

@router.get("/")
async def home_page():
     return {"greeting":"Hello world"}



def change_datatype(user_input: list[str], alias="user_input"):
    for i in range(len(user_input)):
        if '.' in  user_input[i] and user_input[i].replace(".", "").isnumeric():
            user_input[i] = float(user_input[i])
        elif user_input[i] .isnumeric():
            user_input[i]  = int(user_input[i] )
    return user_input

@router.post("/calculator")
async def polonais_calculator(user_input: list[str], alias="user_input") -> int:
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

# @app.post("/")
# def compute(sequence): #: list) -> int:
#     d = list()
#     for touche in sequence:
#         if isinstance(touche, int):
#             d.append(touche)
#         elif isinstance(touche, str):
#             b, a = d.pop(), d.pop()
#             expr = f"{a} {touche} {b}"
#             d.append(eval(expr))

#             #                raise ValueError(f"Expression invalide: {touche}")
#             print(f"{d}  # {touche}")
#             res = d.pop()
#     return res
