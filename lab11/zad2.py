# Wygeneruj wykres punktowy dla 5 różnych losowych serii
#  z użyciem różnych znaczników i kolorów: https://matplotlib.org/api/markers_api.html

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def randrange(n, vmin, vmax):
    '''
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100

for c, m, zlow, zhigh in [('r', 'o', - 50, - 25), ('b', '^', - 30, - 5)]:
    jeden = randrange(n, 0, 10)
    dwa = randrange(n, 11, 22)
    trzy = randrange(n, 23, 34)
    cztery = randrange(n, 35, 46)
    piec = randrange(n, 47, 58)
    ax.scatter(jeden, dwa, trzy, cztery, piec, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()