import unittest
import fracs


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([1, 2]), 1)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero([1, 2]), 0)

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1, 2], [1, 3]), 1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1, 2]), 1/2)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
