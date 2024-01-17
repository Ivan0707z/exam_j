import unittest
from b19 import fibonacci
class TestFibonacciFunction(unittest.TestCase):

    def test_negative_input(self):
        result = fibonacci(-1)
        self.assertIsNone(result, "Для від'ємного входу повинен повертатися None")

    def test_zero_input(self):
        result = fibonacci(0)
        self.assertIsNone(result, "Для нульового входу повинен повертатися None")

    def test_first_element(self):
        result = fibonacci(1)
        self.assertEqual(result, 0, "Перший елемент Фібоначчі повинен бути 0")

    def test_second_element(self):
        result = fibonacci(2)
        self.assertEqual(result, 1, "Другий елемент Фібоначчі повинен бути 1")

    def test_tenth_element(self):
        result = fibonacci(10)
        self.assertEqual(result, 34, "Десятий елемент Фібоначчі повинен бути 34")

    def test_large_input(self):
        result = fibonacci(50)
        self.assertEqual(result, 7778742049, "50-й елемент Фібоначчі повинен бути 12586269025")

if __name__ == '__main__':
    unittest.main()
