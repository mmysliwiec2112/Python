line = "Lorem GVR ipsum \n dolor GvR sit amet"
split_line = line.split()
for x in range(0, len(split_line)):
    if split_line[x] == "GvR":
        # split_line.remove(x)
        split_line.pop(x)
        split_line.insert(x, "Guido van Rossum")
line = ''.join(f'{str(x)} ' for x in split_line)
print(line)
