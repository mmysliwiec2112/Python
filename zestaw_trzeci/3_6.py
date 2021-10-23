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


if __name__ == '__main__':
    print(square(4, 2))
    print(square(5, 10))
    print(square(3, 7))

