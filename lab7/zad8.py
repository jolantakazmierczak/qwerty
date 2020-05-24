# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

import numpy as np

b = np.arange(9).reshape(3,3)
for a in b:
   print(a)