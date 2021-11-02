def odwracanie_it(L, left, right):
    for x in range(left, (left + right) // 2 + 1):
        L[x], L[right + left - x] = L[right + left - x], L[x]


def odwracanie_rek(L, left, right):
    if left < right:
        odwracanie_rek(L, left + 1, right - 1)
        L[left], L[right] = L[right], L[left]


if __name__ == '__main__':
    L1 = [x for x in range(1, 10)]
    print(f'Transforming list: {L1}')
    odwracanie_it(L1, 3, 6)
    print(f'iterative result: {L1}')
    L1 = [x for x in range(1, 10)]
    odwracanie_rek(L1, 3, 6)
    print(f'recursive result: {L1}')

    L2 = [x for x in range(20)]
    print(f'Transforming list: {L2}')
    odwracanie_it(L2, 11, 19)
    print(f'iterative result: {L2}')
    L2 = [x for x in range(20)]
    odwracanie_rek(L2, 11, 19)
    print(f'recursive result: {L2}')
