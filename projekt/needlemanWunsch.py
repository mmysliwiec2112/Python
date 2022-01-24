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
            temporary_scores = []

    alignment_x = ""
    alignment_y = ""
    i = len(seq_x)
    j = len(seq_y)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and grid[i, j] == (grid[i-1, j-1] + score(seq_x[i - 1], seq_y[j - 1], match, mismatch)):
            alignment_x += seq_x[i - 1]
            alignment_y += seq_y[j - 1]
            i -= 1
            j -= 1
        elif i > 0 and grid[i, j] == (grid[i-1, j] - gap):
            alignment_x += seq_x[i - 1]
            alignment_y += '-'
            i -= 1
        else:
            alignment_x += '-'
            alignment_y += seq_y[j - 1]
            j -= 1
    alignment_x = ''.join(alignment_x)[::-1]
    alignment_y = ''.join(alignment_y)[::-1]
    return '\n'.join([alignment_x, alignment_y])



x = "GATTACA"
y = "GCATGCU"
print(calculate_scores(x, y))
# GATTACA
# GCATGCU

np.random.seed(42)

x = np.random.choice(['A', 'T', 'G', 'C'], 10)
y = np.random.choice(['A', 'T', 'G', 'C'], 10)

str_x = ''
for i in range(len(x)):
    str_x += (x[i])

str_y = ''
for i in range(len(y)):
    str_y += (y[i])

print(str_x)
print(str_y)

print(calculate_scores(x, y))

x = np.random.choice(['A', 'T', 'G', 'C'], 50)
y = np.random.choice(['A', 'T', 'G', 'C'], 50)

for i in range(len(x)):
    str_x += (x[i])

for i in range(len(y)):
    str_y += (y[i])

print(str_x)
print(str_y)

print(calculate_scores(x, y))

print(calculate_scores(x, y, gap=0))

print(calculate_scores(x, y, gap=10))

print(calculate_scores(x, y, mismatch=5))

