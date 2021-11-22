import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.

import unittest


class TestPoint(unittest.TestCase):

    def setUp(self):
        pass

    def test_str(self):
        self.assertEqual(str(Point(1, 1)), '(1, 1)')

    def test_repr(self):
        self.assertEqual(repr(Point(1, 1)), 'Point(1, 1)')

    def test_eq(self):
        self.assertTrue(Point(1, 1) == Point(1, 1))
        self.assertFalse(Point(1, 1) == Point(1, 2))

    def test_ne(self):
        self.assertTrue(Point(1, 1) == Point(1, 2))
        self.assertFalse(Point(1, 1) == Point(1, 1))

    def test_add(self):
        self.assertEqual(Point(1, 1) + Point(1, 3), Point(2, 4))
        self.assertEqual(Point(1, 0) + Point(1, 3), Point(2, 3))
        self.assertEqual(Point(0, 1) + Point(1, 3), Point(1, 4))
        self.assertEqual(Point(1, 1) + Point(1, -3), Point(2, -2))
        self.assertEqual(Point(-1, 1) + Point(-1, 3), Point(-2, 4))
        self.assertEqual(Point(1, 1) + Point(-1, -3), Point(0, -2))

    def test_sub(self):
        self.assertEqual(Point(1, 1) - Point(1, 3), Point(0, -2))
        self.assertEqual(Point(1, 0) - Point(1, 3), Point(0, -3))
        self.assertEqual(Point(0, 1) - Point(1, 3), Point(-1, -2))
        self.assertEqual(Point(1, 1) - Point(1, -3), Point(0, 4))
        self.assertEqual(Point(-1, 1) - Point(-1, 3), Point(0, -2))
        self.assertEqual(Point(1, 1) - Point(-1, -3), Point(2, 4))

    def test_mul(self):
        self.assertEqual(Point(1, 1) * Point(1, 3), 4)
        self.assertEqual(Point(1, 0) * Point(1, 3), 1)
        self.assertEqual(Point(0, 1) * Point(1, 3), 3)
        self.assertEqual(Point(1, 1) * Point(1, -3), -2)
        self.assertEqual(Point(-1, 1) * Point(-1, 3), 4)
        self.assertEqual(Point(1, 1) * Point(-1, -3), -4)

    def test_cross(self):
        self.assertEqual(Point(1, 1).cross(Point(1, 3)), 2)
        self.assertEqual(Point(1, 0).cross(Point(1, 3)), 3)
        self.assertEqual(Point(0, 1).cross(Point(1, 3)), -1)
        self.assertEqual(Point(1, 1).cross(Point(1, -3)), -4)
        self.assertEqual(Point(-1, 1).cross(Point(-1, 3)), -2)
        self.assertEqual(Point(1, 1).cross(Point(-1, -3)), -2)

    def test_length(self):
        self.assertEqual(Point(1, 2).length(), math.sqrt(5))
        self.assertEqual(Point(-2, 1).length(), math.sqrt(5))
        self.assertEqual(Point(0, -3).length(), 3)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
