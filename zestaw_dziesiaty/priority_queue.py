import random


class PriorityQueue:
    class PriorityQueueSizeError(Exception):
        def __init__(self):
            pass

        def __str__(self):
            return "cos"

    def __init__(self, size=10):
        self.items = size * [None]
        for x in range(size):
            self.items[x] = -1
        self.n = 0  # pierwszy wolny indeks
        self.size = size
        self.priorities = size * [None]

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def insert(self, data):
        if self.n == self.size:
            raise PriorityQueue.PriorityQueueSizeError
        self.items[self.n] = data
        self.n += 1
        self.items.sort(reverse=True)

    def remove(self):
        if self.n == 0:
            raise PriorityQueue.PriorityQueueSizeError
        self.n -= 1
        return self.items.pop(0)


import unittest


class TestPrioQueue(unittest.TestCase):

    def setUp(self):
        pass

    def testPrioQueue(self):
        prio_que = PriorityQueue(10)
        for x in range(10):
            print(x)
            prio_que.insert(random.randint(0, 100))
        print(prio_que)
        for x in range(10):
            print(prio_que.remove())

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
