line = "Lorem ipsum \n doloro sit amet"
line = line.split()
line.sort()
print(f'Line sorted in alphabetical way: {line}')
line.sort(key=len)
print()
print(f'Line sorted by length of a word: {line}')
