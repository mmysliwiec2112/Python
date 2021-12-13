import nodeTree as nt

def count_leaves(top):
    if top.left is None and top.right is None:
        return 1
    elif top.left is None:
        return count_leaves(top.right)
    elif top.right is None:
        return count_leaves(top.left)
    else:
        return count_leaves(top.left) + count_leaves(top.right)


def count_total(top):
    if top.left is None and top.right is None:
        return top.data
    elif top.left is None:
        return count_total(top.right) + top.data
    if top.right is None:
        return count_total(top.left) + top.data
    else:
        return count_total(top.left) + count_total(top.right) + top.data


import unittest


class TestTree(unittest.TestCase):

    def setUp(self): pass

    def testTree(self):
        root = nt.Node(1)
        root.left = nt.Node(2)
        root.right = nt.Node(3)
        root.right.left = nt.Node(4)
        root.right.right = nt.Node(5)
        root.right.right.left = nt.Node(6)
        root.right.right.right = nt.Node(7)
        root.left.right = nt.Node(8)
        root.left.left = nt.Node(9)
        self.assertEqual(count_leaves(root), 5)
        self.assertEqual(count_total(root), 45)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
