import random as rand


class RandomQueue:
    class RandomQueueSizeError(Exception):
        def __init__(self):
            pass

        def __str__(self):
            return "dodanie elementu do pełnej kolejki lub usunięcie elementu z pustej"

    def __init__(self, size=5):
        self.size = size
        self.items = self.size * [None]
        self.n = 0

    def insert(self, item):
        if self.is_full():
            raise RandomQueue.RandomQueueSizeError
        self.items[self.n] = item
        self.n += 1

    def remove(self):  # zwraca element <- zmien zwracany element na losowy
        if self.is_empty():
            raise RandomQueue.RandomQueueSizeError
        self.n -= 1
        index = rand.randint(0, self.n)
        val = self.items[index]
        self.items[index] = self.items[self.n]
        self.items[self.n] = None

        return val

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.n == self.size

    def clear(self):
        self.items = self.size * [None]
        self.n = 0


import unittest


class TestRandQueue(unittest.TestCase):

    def setUp(self):
        pass

    def testRandomQueue(self):
        rand_que = RandomQueue(10)
        for x in range(10):
            rand_que.insert(x)
        for x in range(10):
            print(rand_que.remove())

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
