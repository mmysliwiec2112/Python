import math


def add_frac(frac1, frac2):
    if frac1[1] == frac2[1]:
        return [frac1[0] + frac2[0], frac1[1] + frac2[1]]
    else:
        n_frac1 = [frac1[0] * frac2[1], frac1[1] * frac2[1]]
        n_frac2 = [frac1[1] * frac2[0], frac1[1] * frac2[1]]
        result = [n_frac1[0] + n_frac2[0], n_frac1[1]]
        gcd = math.gcd(result[0], result[1])
        return [result[0] / gcd, result[1] / gcd]


def sub_frac(frac1, frac2):
    if frac1[1] == frac2[1]:
        return [frac1[0] - frac2[0], frac1[1] - frac2[1]]
    else:
        n_frac1 = [frac1[0] * frac2[1], frac1[1] * frac2[1]]
        n_frac2 = [frac1[1] * frac2[0], frac1[1] * frac2[1]]
        result = [n_frac1[0] - n_frac2[0], n_frac1[1]]
        gcd = math.gcd(result[0], result[1])
        return [result[0] / gcd, result[1] / gcd]


def mul_frac(frac1, frac2):
    result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    gcd = math.gcd(result[0], result[1])
    return [result[0] / gcd, result[1] / gcd]


def div_frac(frac1, frac2):
    result = [frac1[0] * frac2[1], frac1[1] * frac2[0]]
    gcd = math.gcd(result[0], result[1])
    return [result[0] / gcd, result[1] / gcd]


def is_positive(frac):
    if frac[0] > 0 and frac[1] > 0:
        return True
    else:
        return False


def is_zero(frac):
    if frac[0] == 0 and frac[1] != 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):
    n_frac1 = [frac1[0] * frac2[1], frac1[1] * frac2[1]]
    n_frac2 = [frac1[1] * frac2[0], frac1[1] * frac2[1]]
    if n_frac1[0] > n_frac2[0]:
        return 1
    elif n_frac1[0] == n_frac2[0]:
        return 0
    else:
        return -1


def frac2float(frac): return frac[0] / frac[1]


f1 = [-1, 2]  # -1/2
f2 = [0, 1]  # zero
f3 = [3, 1]  # 3
f4 = [6, 2]  # 3 (niejednoznaczność)
f5 = [0, 2]  # zero (niejednoznaczność)
