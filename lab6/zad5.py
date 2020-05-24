# Napisz funkcję, która:

# na wejściu przyjmuje jeden parametr określający długość wektora,
# na podstawie parametru generuje wektor, ale w kolejności odwróconej (czyli np. dla n=3 =>[3 2 1])
# generuje macierz diagonalną z w/w wektorem jako przekątną

import numpy as np

def fun(n):
    A = np.arange(1, n+1)
    B = sorted(A, reverse=True)
    print(f"Wektor:\n{B}")
    B_diag = np.diag(B)
    print(f"Macierz:\n{B_diag}")

print(fun(5))