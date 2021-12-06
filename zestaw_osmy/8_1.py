def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0:
        if b == 0:
            if c == 0:
                print('x i y są rzeczywiste')
            else:
                print('równanie nie ma rozwiązań, jest sprzeczne')
        else:
            if c == 0:
                print('x jest rzeczywiste, a y = 0')
            else:
                print(f'x jest rzeczywiste, a y = {-c / b}')
    else:
        if b == 0:
            if c == 0:
                print('x = 0, a y jest rzeczywiste')
            else:
                print(f' x = {-c / a}, a y jest rzeczywiste')
        else:
            print(f'x jest rzeczywiste, a y = {-a / b} * x / + ({-c / b})')


import unittest


class TestLin(unittest.TestCase):

    def setUp(self): pass

    def testLin(self):
        solve1(1, 2, 3)
        solve1(3, 0, 5)
        solve1(0, 4, 7)
        solve1(1, 1, 0)
        solve1(6, 9, -5)
        solve1(-1, -1, -2)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
