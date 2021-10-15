L = []
for x in range(0, 100):
    L.append(x)
print(L)
L_as_string = ''.join(str(x) for x in L)
print(L_as_string)
