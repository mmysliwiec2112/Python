import os
import random
import unittest

import matplotlib.pyplot as plt

import random_list_generator


def bubblesort(arr):
    n = len(arr)
    before_sorting(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    after_sorting(arr)


def before_sorting(arr):
    print(arr)
    file1 = open("before.dat", "w")

    list_str = build_string(arr)
    file1.write(list_str)
    n = 20
    x = list(range(n))
    y = arr

    plt.title("Sortowanie X")
    plt.xlabel("numer pozycji")
    plt.ylabel("liczba na pozycji")
    plt.plot(x, y, 'rs')  # red squares
    plt.show()
    plt.savefig("plot2.png")  # zapis rysunku do pliku PNG


def after_sorting(arr):
    file1 = open("after.dat", "w")

    list_str = build_string(arr)
    file1.write(list_str)
    n = 20
    x = list(range(n))
    y = arr

    plt.title("Posortowane X")
    plt.xlabel("numer pozycji")
    plt.ylabel("liczba na pozycji")
    plt.plot(x, y, 'rs')  # red squares
    plt.show()
    plt.savefig("plot1.png")  # zapis rysunku do pliku PNG


def build_string(L):
    str = ""
    for x in range(len(L)):
        str += f'{x} {L[x]}\n'
    str += "\n"
    return str


class QuickSortTest(unittest.TestCase):
    def setUp(self):
        self.random_list = random_list_generator.RandomListGenerator()

    def test_totally_random(self):
        bubblesort(self.random_list.totally_random(20))

    def test_almost_sorted(self):
        bubblesort(self.random_list.almost_sorted(20))

    def test_reversed(self):
        bubblesort(self.random_list.reversed(20))

    def test_gaussian(self):
        bubblesort(self.random_list.randomized_gaussian_dist(20))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
