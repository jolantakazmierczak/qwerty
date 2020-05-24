# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.

import numpy as np
import math

a=np.array([3,4,7,1.5,1,math.sqrt(3)/2]).reshape(2, 3)
b=np.sin(a)
print(b)