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
    print(ruler(10))
    print(ruler(15))
    print(ruler(129))
