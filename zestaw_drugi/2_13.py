line = "Lorem ipsum \n dolor sit amet"
line = line.split()
length = [len(line[each]) for each in range(0, len(line))]
print(length)
