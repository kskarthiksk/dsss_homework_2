import unittest
from math_quiz import random_number, choose_operation, format_problem, calculation


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operation(self):
        # Test if the operations are correct
        for _ in range(100):
             operation = choose_operation()
             self.assertTrue(operation in ['+', '-', '*'])

    def test_format_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (7, 3, '*', '7 * 3', 21),
                (6, 4, '-', '6 - 4', 2),
                (3, 2, '*', '3 * 2', 6)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                self.assertTrue(format_problem(num1, num2, operator) == expected_problem and 
                                calculation(num1, num2, operator) == expected_answer)

if __name__ == "__main__":
    unittest.main()
