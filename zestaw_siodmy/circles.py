import math

from zestaw_szosty import point


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = point.Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.pt.x}, {self.pt.y}, {self.radius})'

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return self.radius ** 2 * math.pi

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        if self.radius < other.radius:
            center_dist = ((other.pt.x - self.pt.x) ** 2 + (other.pt.y - self.pt.y) ** 2) ** 0.5
            if center_dist + self.radius <= other.radius:
                return other
            else:
                theta = 1 / 2 + (other.radius - self.radius) / (2 * center_dist)
                center_x = (1 - theta) * self.pt.x + theta * other.pt.x
                center_y = (1 - theta) * self.pt.y + theta * other.pt.y
                return Circle(center_x, center_y, (center_dist + self.radius + other.radius) / 2)
        else:
            center_dist = ((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2) ** 0.5
            if center_dist + other.radius <= self.radius:
                return self
            else:
                theta = 1 / 2 + (self.radius - other.radius) / (2 * center_dist)
                center_x = (1 - theta) * other.pt.x + theta * self.pt.x
                center_y = (1 - theta) * other.pt.y + theta * self.pt.y
                return Circle(center_x, center_y, (center_dist + other.radius + self.radius) / 2)


# Kod testujący moduł.
import unittest


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(0, 5, 2)
        self.c2 = Circle(2, 6, 8)
        self.c3 = Circle(3, 5, 2)

    def test_repr(self):
        self.assertEqual(repr(self.c1), 'Circle(0, 5, 2)')
        self.assertEqual(repr(self.c2), 'Circle(2, 6, 8)')
        self.assertEqual(repr(self.c3), 'Circle(3, 5, 2)')

    def test_eq(self):
        self.assertFalse(self.c1 == self.c1)
        self.assertFalse(self.c1 == self.c2)
        self.assertFalse(self.c2 == self.c3)

    def test_ne(self):
        self.assertFalse(self.c1 != self.c1)
        self.assertTrue(self.c1 != self.c2)
        self.assertTrue(self.c2 != self.c3)

    def test_area(self):
        self.assertEqual(self.c1.area(), math.pi * 2 ** 2)
        self.assertEqual(self.c2.area(), math.pi * 8 ** 2)
        self.assertEqual(self.c3.area(), math.pi * 2 ** 2)

    def test_move(self):
        self.assertEqual(self.c1.move(-self.c1.pt.x, -self.c1.pt.y), Circle(0, 0, 2))
        self.assertEqual(self.c2.move(-self.c2.pt.x, -self.c2.pt.y), Circle(0, 0, 8))
        self.assertEqual(self.c3.move(-self.c3.pt.x, -self.c3.pt.y), Circle(0, 0, 2))

    def test_cover(self):
        self.assertEqual(self.c1.cover(self.c1), self.c1)
        self.assertEqual(self.c2.cover(self.c2), self.c2)
        self.assertEqual(self.c3.cover(self.c3), self.c3)
        self.assertEqual(Circle(0, 0, 28).cover(Circle(1, 1, 1)), Circle(0, 0, 28))
        self.assertEqual(Circle(0, 0, 10).cover(Circle(10, 0, 10)), Circle(5, 0, 15))


if __name__ == "__main__":
    unittest.main()
