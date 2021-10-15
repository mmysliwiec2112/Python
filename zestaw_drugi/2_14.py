line = "Lorem ipsum \n doloro sit amet"
# I added 'o' in word 'dolor' to get one longest word with length of 6
line = line.split()
length = [len(line[each]) for each in range(0, len(line))]
for each in range(0, len(line)):
    if max(length) == len(line[each]):
        print(line[each])
print(max(length))
