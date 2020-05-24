# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?


import numpy as np

a = np.arange(81).reshape(9,9)
print(a)

print("spłaszczanie macierzy:")
e = a.ravel()
print(e)
print("transpozycja macierzy:")
f = a.T
print(f)
