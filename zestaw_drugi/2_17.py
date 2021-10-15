line = "Lorem ipsum \n doloro sit amet"
line = line.split()
line.sort()
print(line)
line.sort(key=len)
print()
print(line)
