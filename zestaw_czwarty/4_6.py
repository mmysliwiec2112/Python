def sum_seq(sequence):
    output = 0
    for x in sequence:
        if isinstance(x, (list, tuple)):
            output += sum_seq(x)
        else:
            output += x
    return output


if __name__ == '__main__':
    test_sequence = [1, (2, 3), [], [4, (5, (6, 7))], 8, [9]]
    print(f'Sum of elements from sequence: [1, (2, 3), [], [4, (5, (6, 7))], 8, [9]] = {sum_seq(test_sequence)}')
    