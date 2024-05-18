import unittest
import math
from shape import Shape, Circle, Square

class TestShape(unittest.TestCase):
    def test_name(self):
        shape = Shape()
        self.assertEqual(shape.name, "Shape")

    def test_area(self):
        shape = Shape()
        self.assertEqual(shape.area(), None)


class TestCircle(unittest.TestCase):
    def test_name(self):
        circle = Circle(1)
        self.assertEqual(circle.name, "Circle")

    def test_area(self):
        circle = Circle(1)
        self.assertEqual(circle.area(), 2 * math.pi)


class TestSquare(unittest.TestCase):
    def test_invalid_side(self):
        self.assertRaises(Exception, lambda: Square(None))

    def test_area(self):
        square = Square(3)
        self.assertEqual(square.area(), 4 * 3) 