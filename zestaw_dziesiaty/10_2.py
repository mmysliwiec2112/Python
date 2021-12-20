class Stack:
    class StackSizeError(Exception):
        def __init__(self):
            pass

        def __str__(self):
            return "cos"

    def __init__(self, size=10):
        self.items = size * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.n == self.size:
            raise Stack.StackSizeError
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.n == 0:
            raise Stack.StackSizeError
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None  # usuwam referencję
        return data


import unittest


class TestList(unittest.TestCase):

    def setUp(self): pass

    def testSizeError(self):
        stack = Stack(3)
        # self.assertRaises(ZeroDivisionError)
        # 100 / 0
        with self.assertRaises(Stack.StackSizeError):
            stack.pop()
        for i in range(3):
            stack.push(i)
        with self.assertRaises(Stack.StackSizeError):
            stack.push(5)
        for i in range(3):
            stack.pop()
        with self.assertRaises(Stack.StackSizeError):
            stack.pop()

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
