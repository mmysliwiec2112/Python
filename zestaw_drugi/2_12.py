line = "Lorem ipsum \n dolor sit amet"
split_line = line.split()

first_letters_line = ""
for each in range(0, len(split_line)):
    first_letters_line += split_line[each][0]

last_letters_line = ""
for each in range(0, len(split_line)):
    last_letters_line += split_line[each][-1]

print(f' Line split into list: {split_line}')
print(f' Word created from first letters of words in the line: {first_letters_line}')
print(f' Word created from last letters of words in the line: {last_letters_line}')
