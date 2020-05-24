# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite,
#  a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.

import numpy as np
import math

a=np.array([1, 3, 6])
b=np.array([1.1, -2, math.sqrt(3)])


print(a*b)