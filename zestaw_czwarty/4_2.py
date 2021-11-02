def square(x, y):
    output = ""
    for each in range(0, x):
        output += '+---'
    output += '+\n'
    for y in range(0, y):
        for each in range(0, x):
            output += '|   '
        output += '|\n'
        for each in range(0, x):
            output += '+---'
        output += '+\n'
    return output


def ruler(length):
    output = ""
    numbers = ""
    # pierwsza linia:
    for x in range(0, length + 1):
        output += '|....'
    output += '|\n '
    # druga linia:
    for x in range(0, length + 1):
        output += str(x).rjust(5)
    return output


if __name__ == '__main__':
    print(f'Tests for rulers of different length')
    print(ruler(10))
    print(ruler(15))
    print(ruler(129))
    print(f'Tests for squares of different size')
    print(square(4, 2))
    print(square(5, 10))
    print(square(3, 7))
