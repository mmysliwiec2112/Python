#
# niepoprawne jest pisanie wielu przypisań w jednej linii
# L = [3, 5, 4] ; L = L.sort()
# jest zbyt dużo wartości do przypisania w stosunku do zmiennych
# x, y = 1, 2, 3
# krotki nie wspierają przypisywania nowych elementow
# X = 1, 2, 3 ; X[1] = 4
# indeks 3 jest poza zasięgiem
# X = [1, 2, 3] ; X[3] = 4
# klasa str nie ma implementacji funkcji append
# X = "abc" ; X.append("d")
# range(8) nie jest iterable (?)
# L = list(map(pow, range(8)))