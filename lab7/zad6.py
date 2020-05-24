# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.

import numpy as np


a=np.array([1,3,8,1,-9,3]).reshape(2, 3)
b=np.cos(a)
print(b)