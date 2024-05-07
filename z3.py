import unittest
import sys
from timeit import default_timer as timer

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFact(unittest.TestCase):
    
    def test_plus(self):
        self.assertEqual(factorial(4),24)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_minus(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_big(self):
        self.assertEqual(factorial(10), 3628800)

    def test_too_big(self):
        with self.assertRaises(ValueError):
            factorial(1000)

if __name__ == "__main__":
    start = timer()
    unittest.main()
    end = timer()







