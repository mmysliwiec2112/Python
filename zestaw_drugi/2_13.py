line = "Lorem ipsum \n dolor sit amet"
line = line.split()
length = [len(line[each]) for each in range(0, len(line))]
print(f'An array with lengths of each words: {length}')
print(f'Total sum of lengths of words: {sum(length)}')
