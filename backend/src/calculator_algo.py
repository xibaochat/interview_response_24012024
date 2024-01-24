import math
from typing import Union, List

ERROR = 0
OK = 1

def get_ops(arr):
    if len(arr) < 2:
        return ERROR
    n1 = arr.pop()
    n2 = arr.pop()
    return OK, n1, n2


def solve(arr, oper):
    flag, n1, n2 = get_ops(arr)
    if flag:
        if oper == '+':
            arr.append(n2 + n1)
        elif oper == '-':
            arr.append(n2 - n1)
        elif oper == '*':
            arr.append(n2 * n1)
        elif oper == '/':
            if not n1:
                return ERROR
            else:
                arr.append(n2 / n1)
        elif oper == '^':
            arr.append(math.pow(n2, n1))
    else:
        return ERROR
    return OK

def calculator(instruction: List[Union[int, str]]) -> int:
    arr = []
    for ele in instruction:
        print(f"ele is {ele}")
        if ele in ['+', '-', '*', '/', '^']:
            solve(arr, ele)
        else:
            arr.append(float(ele))
    res = arr[-1]
    return res
