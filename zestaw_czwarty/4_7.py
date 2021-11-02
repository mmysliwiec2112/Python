def flatten(sequence):
    output = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            output += flatten(x)
        else:
            output.append(x)
    return output


if __name__ == '__main__':
    test_sequence = [1, (2, 3), [], [4, (5, (6, 7))], 8, [9]]
    print(f'Flatten sequence: [1, (2, 3), [], [4, (5, (6, 7))], 8, [9]] = {flatten(test_sequence)}')
