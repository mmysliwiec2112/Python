import nodeList as nl


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        node = self.head
        list_str = ""
        while node:
            list_str += str(node) + " "
            node = node.next
        return list_str

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.next = node
            self.tail = node

        # print(f"node {node} == head {self.head}")
        # if node == self.head:
        #     self.tail.next = node
        #     self.tail = node
        #     self.remove_head()

        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            while node.next != self.tail:
                node = node.next
            self.tail = node
        node.next = None
        self.length -= 1

    def join(self, other):
        if self.is_empty():
            raise ValueError("pusta lista")

        self.tail.next = other.head
        self.tail = other.tail
        other.clear()

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def search(self, data):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        while node.data != data:
            node = node.next
        return node

    def find_min(self):
        if self.is_empty():
            return None
        node = self.head
        min_val = node.data
        while node != self.tail:
            node = node.next
            if min_val > node.data:
                min_val = node.data
        return min_val

    def find_max(self):
        if self.is_empty():
            return None
        node = self.head
        max_val = node.data
        while node != self.tail:
            node = node.next
            if max_val < node.data:
                max_val = node.data
        return max_val

    def reverse(self):
        node = self.head
        next = None
        while node is not None:
            prev = node.next
            node.next = next
            next = node
            node = prev
        self.head = next

    def print_list(self):
        node = self.head
        while node:
            print(node)
            node = node.next


import unittest


class TestList(unittest.TestCase):

    def setUp(self):
        self.test_list = SingleList()
        self.test_list.insert_head(nl.Node(2))
        self.test_list.insert_head(nl.Node(1))
        self.test_list.insert_tail(nl.Node(3))
        self.test_list.insert_tail(nl.Node(4))
        self.test_list.insert_head(nl.Node(0))

    def testPrint(self):
        self.assertEqual(str(self.test_list), '0 1 2 3 4 ')

    def testRmTail(self):
        self.test_list.remove_tail()
        self.assertEqual(str(self.test_list), '0 1 2 3 ')

    def testRmHead(self):
        self.test_list.remove_head()
        self.assertEqual(str(self.test_list), '1 2 3 4 ')

    def testJoin(self):
        join_list = SingleList()
        join_list.insert_tail(nl.Node(10))
        join_list.insert_tail(nl.Node(11))
        join_list.insert_tail(nl.Node(12))
        join_list.insert_tail(nl.Node(13))
        join_list.insert_tail(nl.Node(14))

        self.test_list.join(join_list)
        # join_list.remove_head() rzuca ValueError
        self.assertEqual(str(self.test_list), '0 1 2 3 4 10 11 12 13 14 ')

    def testMin(self):
        self.assertEqual(self.test_list.find_min(), 0)

    def testMax(self):
        self.assertEqual(self.test_list.find_max(), 4)

    def testRev(self):
        self.test_list.reverse()
        self.assertEqual(str(self.test_list), '4 3 2 1 0 ')

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
