import numpy as np


def score(val_x, val_y, match, mismatch):
    if val_x == val_y:
        return match
    else:
        return -mismatch


def calculate_scores(seq_x, seq_y, match=1, mismatch=3, gap=4):
    len_x = len(seq_x)
    len_y = len(seq_y)

    # grid for calculation of an optimal alignment
    grid = np.zeros((len_x + 1, len_y + 1))
    grid[:, 0] = np.linspace(0, -len_x * gap, len_x + 1)
    grid[0, :] = np.linspace(0, -len_y * gap, len_y + 1)

    traceback_matrix = [[[] for j in range(len_y + 1)] for i in range(len_x + 1)]

    for i in range(len_x):
        traceback_matrix[i][0] += 'l'
    for i in range(len_y):
        traceback_matrix[0][i] += 'u'

    # Calculating scores.
    temporary_scores = []
    for i in range(1, len_x + 1):
        for j in range(1, len_y + 1):
            # calculating the f matrix value
            temporary_scores.append(grid[i - 1, j - 1] + score(seq_x[i - 1], seq_y[j - 1], match, mismatch))
            temporary_scores.append(grid[i - 1, j] - gap)
            temporary_scores.append(grid[i, j - 1] - gap)
            tmax = np.max(temporary_scores)
            grid[i, j] = tmax

            # adding proper values to the traceback matrix\
            if temporary_scores[0] == tmax:
                traceback_matrix[i][j] += 'd'
            elif temporary_scores[1] == tmax:
                traceback_matrix[i][j] += 'l'
            elif temporary_scores[2] == tmax:
                traceback_matrix[i][j] += 'u'
            temporary_scores = []

    alignment_x = ""
    alignment_y = ""
    control = ''
    i = len(seq_x)
    j = len(seq_y)
    while i > 0 or j > 0:
        if traceback_matrix[i][j] == ['d']:
            alignment_x += seq_x[i - 1]
            alignment_y += seq_y[j - 1]
            control += 'd'
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == ['l']:
            alignment_x += seq_x[i - 1]
            alignment_y += '-'
            control += 'l'
            i -= 1
        elif traceback_matrix[i][j] == ['u']:
            alignment_x += '-'
            alignment_y += seq_y[j - 1]
            control += 'u'
            j -= 1
    alignment_x = ''.join(alignment_x)[::-1]
    alignment_y = ''.join(alignment_y)[::-1]
    print(control)
    return '\n'.join([alignment_x, alignment_y])


def print_results(x, y):
    str_x = ''
    for i in range(len(x)):
        str_x += (x[i])

    str_y = ''
    for i in range(len(y)):
        str_y += (y[i])
    print(f'\n\nalignment for: \nx: {str_x}\ny: {str_y}\n{calculate_scores(x, y)}')

import unittest


class TestList(unittest.TestCase):

    def setUp(self): pass

#wyniki testów sprawdzane przy pomocy strony https://bioboot.github.io/bimm143_W20/class-material/nw/
    def testCalculateScores(self):
        x = "GATTACA"
        y = "GCATGCU"
        self.assertTrue(calculate_scores(x, y), ["GATTACA", "GCATGCU"])

        np.random.seed(32)
        x = np.random.choice(['A', 'T', 'G', 'C'], 10)
        y = np.random.choice(['A', 'T', 'G', 'C'], 5)
        self.assertTrue(calculate_scores(x, y), ["CCTGAGACAC", "-----GTCTG"])

        np.random.seed(32)
        x = np.random.choice(['A', 'T', 'G', 'C'], 10)
        y = np.random.choice(['A', 'T', 'G', 'C'], 10)
        self.assertTrue(calculate_scores(x, y), ["-CCTGAGACAC", "GTCTG-TACTC"])

        np.random.seed(42)
        x = np.random.choice(['A', 'T', 'G', 'C'], 10)
        y = np.random.choice(['A', 'T', 'G', 'C'], 10)
        self.assertTrue(calculate_scores(x, y), ["GCAGGCA-AGT", "G-GGGCACCCG"])

    def tearDown(self): pass


if __name__ == '__main__':

    np.random.seed(42)
    x = np.random.choice(['A', 'T', 'G', 'C'], 50)
    y = np.random.choice(['A', 'T', 'G', 'C'], 50)
    print_results(x, y)

    print('\nresults for gap value equal to 0:')
    print(calculate_scores(x, y, gap=0))

    print('\nresults for gap value equal to 10:')
    print(calculate_scores(x, y, gap=10))

    print('\nresults for mismatch value equal to 5:')
    print(calculate_scores(x, y, mismatch=5))

    unittest.main()




