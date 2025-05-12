# Лабораторная 1 вариант 5
from itertools import product


def generate_strings(alphabet, n):
    alphabet = sorted(alphabet)
    for p in product(alphabet, repeat=n):
        print(''.join(p))

alphabet = input("Введите алфавит (через пробел): ").split()
n = int(input("Введите длину строк: "))

generate_strings(alphabet, n)