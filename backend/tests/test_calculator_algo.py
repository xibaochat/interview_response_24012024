from typing import List, Union
import unittest
from unittest.mock import patch

from parameterized import parameterized

from calculator_algo import (
    CalculationException,
    get_ops,
    solve_operation,
    calculator
)


class TestCalculatorAlgo(unittest.TestCase):
    @parameterized.expand([
        [[41, 1]],
        [[100, 42]],
        [[0, 42, 199]],
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]],
    ])
    def test_get_ops(self, inputs: List[int]):
        mem_inputs = inputs.copy()
        res = get_ops(inputs)
        self.assertEqual(res[0], mem_inputs[-1])
        self.assertEqual(res[1], mem_inputs[-2])

    @parameterized.expand([
        [[1]],
        [[]],
    ])
    def test_get_ops_exception(self, inputs: List[int]):
        self.assertRaises(CalculationException, get_ops, inputs)

    @parameterized.expand([
        [[41, 1], '+', 42],
        [[41, 1], '-', 40],
        [[41, 1], '*', 41],
        [[41, 1], '/', 41],
        [[41, 1], '^', 41],

        [[41, 2], '+', 43],
        [[41, 2], '-', 39],
        [[41, 2], '*', 82],
        [[41, 2], '/', 20.5],
        [[41, 2], '^', 1681],

        [[41.5, 1], '+', 42.5],
        [[41.5, 1], '-', 40.5],
        [[41.5, 1], '*', 41.5],
        [[41.5, 1], '/', 41.5],
        [[41.5, 1], '^', 41.5],

        [[41.5, 2], '+', 43.5],
        [[41.5, 2], '-', 39.5],
        [[41.5, 2], '*', 83.0],
        [[41.5, 2], '/', 20.75],
        [[41.5, 2], '^', 1722.25],
    ])
    def test_solve_operation(self, inputs: List[int], operator: str, expected_res: Union[int, float]):
        solve_operation(inputs, operator)
        self.assertEqual(inputs[-1], expected_res)

    def test_solve_operation_exception(self):
        self.assertRaises(CalculationException, solve_operation, [42, 0], '/')

    @patch('calculator_algo.solve_operation')
    def test_calculator(self, mock_solve_operation):
        res = calculator([41, 1, '+'])
        self.assertTrue(mock_solve_operation.called_once)

    @parameterized.expand([
        [[41, 'invalid', '+']],
        [['invalid', 41, '+']],
        [[41, 1, 'invalid']],
    ])
    def test_calculator_raise(self, instruction: List[Union[int, float, str]]):
        self.assertRaises(CalculationException, calculator, instruction)


if __name__ == '__main__':
    unittest.main()
