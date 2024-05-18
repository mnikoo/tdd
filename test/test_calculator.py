import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(1.5, 2), -0.5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)

    def test_multiply2(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertRaises(ZeroDivisionError, lambda: self.calculator.divide(2, 0))