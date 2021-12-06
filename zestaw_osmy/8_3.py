import math
import random
import unittest


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    # Number of darts that land inside.
    inside = 0
    for i in range(0, n):
        x2 = random.random() ** 2
        y2 = random.random() ** 2
        if math.sqrt(x2 + y2) < 1.0:
            inside += 1
    pi = (float(inside) / n) * 4
    print(f' obliczone pi: {pi}, vs prawdziwa wartość pi: {math.pi}, błąd: {abs(pi-math.pi)}')


class TestMonteCarlo(unittest.TestCase):

    def setUp(self): pass

    def testMonteCarlo(self):
        calc_pi()
        calc_pi(1000)
        calc_pi(10000)
        calc_pi(100000)
        calc_pi(1000000)
        calc_pi(10000000)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
