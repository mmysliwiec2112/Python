def sum_tuples(x):
    output = []
    temp = 0
    for each in range(0, len(x)):
        for each2 in range(0, len(x[each])):
            temp += x[each][each2]
        output.append(temp)
        temp = 0
    return output


if __name__ == '__main__':
    print(sum_tuples([[], [4], (1, 2), [3, 4], (5, 6, 7)]))
