# Napisz funkcję, która będzie:

# przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
import numpy as np

def fun(n):
    A = np.arange(1, n*n+1)
    B = A.reshape(n, n)
    print(B)


fun(5)