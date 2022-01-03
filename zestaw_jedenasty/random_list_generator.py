import random
import unittest

import numpy


class RandomListGenerator:
    def __init__(self):
        pass

    # różne liczby int od 0 do n - 1 w kolejności losowej,
    def totally_random(self, n):
        temp = [x for x in range(n)]
        random.shuffle(temp)
        return temp

    # różne liczby int od 0 do n-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji)
    def almost_sorted(self, n):
        temp = [x for x in range(n)]
        n *= 0.1
        n = int(n)
        if n < 1.0:
            n = 1
        for x in range(n):
            pos1 = random.randint(0, len(temp) - 1)
            pos2 = random.randint(0, len(temp) - 2)
            if pos1 == pos2:
                pos2 += 1
            self.swap(temp, pos1, pos2)
        return temp

    def reversed(self, n):
        temp = [n - x - 1 for x in range(n)]
        return temp

    def randomized_gaussian_dist(self, n):
        temp = numpy.random.normal(size=n)
        lista = []
        while len(temp) != 0:
            index = random.randint(0, len(temp) - 1)
            lista.append(temp[index])
            temp = numpy.delete(temp, index)
        return lista

    def swap(self, list, a, b):
        list[a], list[b] = list[b], list[a]


class RandomListTest(unittest.TestCase):
    def setUp(self):
        self.random_list = RandomListGenerator()

    def test_totally_random(self):
        print("totally random")
        print(self.random_list.totally_random(10))
        print(self.random_list.totally_random(20))
        print(self.random_list.totally_random(15))
        print(self.random_list.totally_random(5))

    def test_almost_sorted(self):
        print("almost sorted")
        print(self.random_list.almost_sorted(10))
        print(self.random_list.almost_sorted(20))
        print(self.random_list.almost_sorted(15))
        print(self.random_list.almost_sorted(5))

    def test_reversed(self):
        print("reversed")
        print(self.random_list.reversed(10))
        print(self.random_list.reversed(20))
        print(self.random_list.reversed(15))
        print(self.random_list.reversed(5))

    def test_gaussian(self):
        print("gaussian")
        print(self.random_list.randomized_gaussian_dist(10))
        print(self.random_list.randomized_gaussian_dist(20))
        print(self.random_list.randomized_gaussian_dist(15))
        print(self.random_list.randomized_gaussian_dist(5))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
