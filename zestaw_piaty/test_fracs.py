import unittest
import fracs


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([1, 3], [1, 4]), [7, 12])
        self.assertEqual(fracs.add_frac([-1, 2], [1, 3]), [-1, 6])
        self.assertEqual(fracs.add_frac([1, 2], [-1, 3]), [1, 6])
        self.assertEqual(fracs.add_frac([1, 3], [1, 3]), [2, 3])


    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.sub_frac([1, 3], [1, 4]), [1, 12])
        self.assertEqual(fracs.sub_frac([-1, 2], [1, 3]), [-5, 6])
        self.assertEqual(fracs.sub_frac([1, 2], [-1, 3]), [5, 6])
        self.assertEqual(fracs.sub_frac([1, 3], [1, 3]), [0, 0])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.mul_frac([1, 3], [1, 4]), [1, 12])
        self.assertEqual(fracs.mul_frac([-1, 2], [1, 3]), [-1, 6])
        self.assertEqual(fracs.mul_frac([1, 2], [-1, 3]), [-1, 6])
        self.assertEqual(fracs.mul_frac([1, 3], [1, 3]), [1, 9])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(fracs.div_frac([1, 3], [1, 4]), [4, 3])
        self.assertEqual(fracs.div_frac([-1, 2], [1, 3]), [-3, 2])
        self.assertEqual(fracs.div_frac([1, 2], [-1, 3]), [-3, 2])
        self.assertEqual(fracs.div_frac([1, 3], [1, 3]), [1, 1])


    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([1, 2]), 1)
        self.assertEqual(fracs.is_positive([1, -2]), 0)
        self.assertEqual(fracs.is_positive([-1, 2]), 0)
        self.assertEqual(fracs.is_positive([-1, -2]), 0)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero([1, 2]), 0)
        self.assertEqual(fracs.is_zero([0, 2]), 1)
        self.assertEqual(fracs.is_zero([1, 0]), 0)
        self.assertEqual(fracs.is_zero([0, 0]), 0)

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(fracs.cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(fracs.cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(fracs.cmp_frac([1, 4], [1, 32]), 1)
        self.assertEqual(fracs.cmp_frac([1, 32], [1, 32]), 0)
        self.assertEqual(fracs.cmp_frac([1, 32], [1, 4]), -1)


    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1, 2]), 1/2)
        self.assertEqual(fracs.frac2float([-1, 2]), -1/2)
        self.assertEqual(fracs.frac2float([1, 1]), 1)
        self.assertEqual(fracs.frac2float([3, 2]), 3/2)
        self.assertEqual(fracs.frac2float([1, -2]), -1/2)


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
