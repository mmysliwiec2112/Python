import random as rand


class PriorityQueue:
    class PriorityQueueSizeError(Exception):
        def __init__(self):
            pass

        def __str__(self):
            return "cos"

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0  # pierwszy wolny indeks
        self.size = size
        self.priorities = size * [None]

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def insert(self, data):
        if self.n == 0:
            raise PriorityQueue.PriorityQueueSizeError
        self.items[self.n] = data
        self.n += 1

    def remove(self):
        if self.n == self.size:
            raise PriorityQueue.PriorityQueueSizeError
        # Etap 1 - wyszukiwanie elementu.
        maxi = 0
        for i in range(self.n):
            if self.items[i] > self.items[maxi]:
                maxi = i
        # Etap 2 - usuwanie elementu.
        self.n -= 1
        data = self.items[maxi]
        self.items[maxi] = self.items[self.n]
        self.items[self.n] = None  # usuwamy referencję
        return data

import unittest


class TestPrioQueue(unittest.TestCase):

    def setUp(self):
        pass

    def testPrioQueue(self):
        prio_que = PriorityQueue(10)
        for x in range(10):
            prio_que.insert(rand.randint(0, 100))
        for x in range(10):
            prio_que.remove()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
