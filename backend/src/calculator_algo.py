import math
from typing import Union, List, Tuple


class CalculationException(Exception):
    pass


def get_ops(arr: List[Union[int, float]]) -> Tuple:
    """
        Pop the numbers to make the calculation with\
        :param (List) arr: object to extract the last two number from
        return (Tuple): poped numbers
    """
    if len(arr) < 2:
        raise CalculationException()

    n1 = arr.pop()
    n2 = arr.pop()
    return n1, n2


def solve_operation(arr: List[Union[int, float]], oper: str):
    """
    Calculate the 2 last poped element then append the result in arr
    """
    n1, n2 = get_ops(arr)
    if oper == '+':
        arr.append(n2 + n1)
    elif oper == '-':
        arr.append(n2 - n1)
    elif oper == '*':
        arr.append(n2 * n1)
    elif oper == '/':
        if n1 == 0:
            raise CalculationException()
        arr.append(n2 / n1)
    elif oper == '^':
        arr.append(math.pow(n2, n1))


def calculator(instruction: List[Union[int, float, str]]) -> float:
    """
    iterate each element, if it's operation then do the calculation,
    if not append the element
    """
    arr = []
    for ele in instruction:
        if ele in ['+', '-', '*', '/', '^']:
            solve_operation(arr, ele)
        else:
            try:
                arr.append(float(ele))
            except ValueError:
                raise CalculationException()
    return arr[-1]
