# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki, 
# gdzie jedno słowo będzie wypisane w kolumnie,
#  jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być wypisane od prawej do lewej.

import numpy as np

def fun(n):
    slowa = ['mordor', 'udhqke', 'cołqwe', 'hreawe', 'afrazs']
    s = [[], [], [], [], []]
    for i in range(0, 5, 1):
        s[i] = np.array(list(slowa[i]))
        s[i] = np.fromiter(slowa[i], dtype='U1')
        print(s[i])

fun(6)

 # mordor 1 linjka, mdła po ukosie, frodo 3 kolumna, szarfa od tylu ostatni wiersz