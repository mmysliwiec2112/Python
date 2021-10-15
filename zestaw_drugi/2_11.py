line = "word"
for x in range(1, 2 * len(line) - 1, 2):
    line = line[:x] + "_" + line[x:]
print(f'Word with sign "_" put between each two of letters: {line}')
