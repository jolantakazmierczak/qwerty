# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# Przy założeniach:

# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n 
# i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.

import numpy as np

def fun(n):
    przek = [2 for x in range(n)]
    A = np.diag(przek)
    for a in range(0, n):
        for b in range(0, n):
            for c in range(1, n+1):
                if(a == b+c or b == a+c):
                    A[a, b] = 2*(c+1)

    print(A)


fun(5)