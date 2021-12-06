import math


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b <= c and a + c <= b and c + b <= a or (a <= 0 or b <= 0 or c <= 0):
        raise ValueError("liczby nie spełniają warunku trójkąta")
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))


import unittest


class TestTriangleArea(unittest.TestCase):

    def setUp(self): pass

    def testTrArea(self):
        heron(1, 1, 1)
        heron(3, 2, 5)
        heron(5, 4, 7)
        heron(1, 2, 2)
        heron(6, 9, 4)
        heron(3, 4, 5)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
