L = []
for x in range(0, 200):
    L.append(str(x))

for x in range(0, len(L)):
    L[x] = L[x].zfill(3)

print(f'List, where each number is filled with zeroes so that each cell has three numbers: \n{L}')

