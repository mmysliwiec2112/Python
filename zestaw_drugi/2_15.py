L = []
for x in range(0, 100):
    L.append(x)
print(f'A list of natural numbers: \n{L}')
L_as_string = ''.join(str(x) for x in L)
print(f'List as a string: \n{L_as_string} \nType of the string: {type(L_as_string)}')
