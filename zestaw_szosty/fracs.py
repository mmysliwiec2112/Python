import math


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y != 1:
            return f'{self.x}/{self.y}'
        else:
            return f'{self.x}'

    def __repr__(self):
        return f'Frac({self.x}, {self.y})'

    def __eq__(self, other):
        return self.cmp_frac(other) == 0

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self.cmp_frac(other) == -1:
            return True
        else:
            return False

    def __le__(self, other):
        if self.cmp_frac(other) != 1:
            return True
        else:
            return False

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        if self.y == other.y:
            self.x += other.x
        else:
            self.x = self.x * other.y + other.x * self.y
            self.y *= other.y
        self.red_frac()
        return Frac(self.x, self.y)

    def __sub__(self, other):
        if self.y == other.y:
            self.x -= other.x
        else:
            self.x = self.x * other.y - other.x * self.y
            self.y *= other.y
        self.red_frac()
        return Frac(self.x, self.y)

    def __mul__(self, other):
        self.x *= other.x
        self.y *= other.y
        self.red_frac()
        return Frac(self.x, self.y)

    def __truediv__(self, other):
        self.x *= other.y
        self.y *= other.x
        self.red_frac()
        return Frac(self.x, self.y)

    def __floordiv__(self, other):
        pass  # frac1 // frac2, opcjonalnie

    def __mod__(self, other):
        pass  # frac1 % frac2, opcjonalnie

    # operatory jednoargumentowe
    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        if self.x > 0:
            return Frac(self.y, self.x)
        elif self.x < 0:
            return Frac(-self.y, -self.x)
        else:
            return Frac(self.x, self.y)

    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))

    def red_frac(self):
        if self.y == 0:
            print('Nie można dzielić przez zero!')
            return
        gcd = math.gcd(self.x, self.y)
        self.x, self.y = self.x / gcd, self.y / gcd

        if self.x > 0 > self.y:
            self.x, self.y = self.x * (-1), self.y

    def cmp_frac(self, other):
        frac1 = Frac(self.x * other.y, self.y * other.y)
        frac2 = Frac(other.x * self.y, other.y * self.y)
        if frac1.x > frac2.x:
            return 1
        elif frac1.x == frac2.x:
            return 0
        else:
            return -1


# Kod testujący moduł.

import unittest


class TestFrac(unittest.TestCase):

    def setUp(self):
        pass

    def test_eq(self):
        self.assertTrue(Frac(1, 2) == Frac(1, 2))
        self.assertFalse(Frac(1, 3) == Frac(1, 2))
        self.assertTrue(Frac(0, 2) == Frac(0, 3))

    def test_str(self):
        self.assertEqual(str(Frac(1, 2)), '1/2')

    def test_repr(self):
        self.assertEqual(repr(Frac(1, 2)), 'Frac(1, 2)')

    def test_ne(self):
        self.assertFalse(Frac(1, 2) != Frac(1, 2))
        self.assertTrue(Frac(1, 3) != Frac(1, 2))
        self.assertFalse(Frac(0, 2) != Frac(0, 3))

    def test_lt(self):
        self.assertFalse(Frac(1, 2) < Frac(1, 2))
        self.assertTrue(Frac(1, 3) < Frac(1, 2))
        self.assertFalse(Frac(0, 2) < Frac(0, 3))

    def test_le(self):
        self.assertTrue(Frac(1, 2) <= Frac(1, 2))
        self.assertFalse(Frac(1, 2) <= Frac(1, 3))
        self.assertTrue(Frac(0, 2) <= Frac(0, 3))

    def test_gt(self):
        self.assertFalse(Frac(1, 2) > Frac(1, 2))
        self.assertTrue(Frac(1, 2) > Frac(1, 3))
        self.assertFalse(Frac(0, 2) > Frac(0, 3))

    def test_ge(self):
        self.assertTrue(Frac(1, 2) >= Frac(1, 2))
        self.assertFalse(Frac(1, 3) >= Frac(1, 2))
        self.assertTrue(Frac(0, 2) >= Frac(0, 3))

    def test_pos(self):
        self.assertEqual(+Frac(1, 2), Frac(1, 2))
        self.assertEqual(+Frac(-1, 2), Frac(-1, 2))

    def test_neg(self):
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertEqual(-Frac(-1, 2), Frac(1, 2))

    def test_inv(self):
        self.assertEqual(~Frac(1, 2), Frac(2, 1))
        self.assertEqual(~Frac(-1, 2), Frac(-2, 1))
        self.assertEqual(~Frac(0, 2), Frac(0, 1))

    def test_float(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)

    def test_hash(self):
        self.assertEqual(Frac(2, 3), Frac(2.0, 3.0))

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(1, 3) + Frac(1, 4), Frac(7, 12))
        self.assertEqual(Frac(-1, 2) + Frac(1, 3), Frac(-1, 6))
        self.assertEqual(Frac(1, 3) + Frac(1, 3), Frac(2, 3))
        self.assertEqual(Frac(0, 2) + Frac(1, 3), Frac(1, 3))
        self.assertEqual(Frac(1, 1) + Frac(1, 3), Frac(4, 3))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(1, 3) - Frac(1, 4), Frac(1, 12))
        self.assertEqual(Frac(-1, 2) - Frac(1, 3), Frac(-5, 6))
        self.assertEqual(Frac(1, 3) - Frac(1, 3), Frac(0, 9))
        self.assertEqual(Frac(0, 2) - Frac(1, 3), Frac(-1, 3))
        self.assertEqual(Frac(1, 1) - Frac(1, 3), Frac(2, 3))

    def test_mul(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(12, 3) * Frac(5, 4), Frac(60, 12))
        self.assertEqual(Frac(-1, 2) * Frac(1, 3), Frac(-1, 6))
        self.assertEqual(Frac(1, 3) * Frac(1, 3), Frac(1, 9))
        self.assertEqual(Frac(0, 2) * Frac(1, 3), Frac(0, 5))
        self.assertEqual(Frac(1, 1) * Frac(1, 3), Frac(1, 3))

    def test_div(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 3), Frac(3, 2))
        self.assertEqual(Frac(12, 3) / Frac(5, 4), Frac(48, 15))
        self.assertEqual(Frac(-1, 2) / Frac(1, 3), Frac(-3, 2))
        self.assertEqual(Frac(1, 3) / Frac(1, 3), Frac(1, 1))
        self.assertEqual(Frac(0, 2) / Frac(1, 3), Frac(0, 5))
        self.assertEqual(Frac(1, 1) / Frac(1, 3), Frac(3, 1))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
