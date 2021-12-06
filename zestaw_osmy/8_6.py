import time


def dynamic(i, j):
    num_vals = [[]]
    num_vals[0].append(0.5)
    for z in range(1, j + 1):
        num_vals[0].append(0.0)
    for x in range(1, i + 1):
        num_vals.append([])
        num_vals[x].append(1.0)
        for y in range(1, j + 1):
            num_vals[x].append(0.5 * (num_vals[x - 1][y] + num_vals[x][y - 1]))
    return num_vals[i][j]


def recursion(i, j):
    if i == 0 and j == 0:
        return 0.5
    if i == 0 and j > 0:
        return 0.0
    if i > 0 and j == 0:
        return 1.0
    if i > 0 and j > 0:
        return 0.5 * (recursion(i - 1, j) + recursion(i, j - 1))


import unittest


class TestDynamic(unittest.TestCase):

    def setUp(self): pass

    def testDynamic(self):
        self.assertEqual(recursion(1, 1), dynamic(1, 1))
        self.assertEqual(recursion(3, 5), dynamic(3, 5))
        self.assertEqual(recursion(5, 7), dynamic(5, 7))
        self.assertEqual(recursion(1, 2), dynamic(1, 2))
        self.assertEqual(recursion(6, 9), dynamic(6, 9))
        self.assertEqual(recursion(4, 5), dynamic(4, 5))

        print("Porownanie czasu dla wywolan funkcji z takimi samymi argumentami:")
        rekurencyjnie_start = time.time()
        recursion(13, 13)
        print("Czas dla metody rekurencyjnej: ", f"{time.time() - rekurencyjnie_start}s")

        dynamicznie_start = time.time()
        dynamic(13, 13)
        print("Czas dla metody dynamicznej: ", f"{time.time() - dynamicznie_start}s")

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
