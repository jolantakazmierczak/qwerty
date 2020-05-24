# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. 
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

import numpy as np

a = np.arange(12).reshape(3, 4)
b = np.arange(12).reshape(4, 3)
c = np.arange(12).reshape(2, 6)
x=a.ravel()
y=b.ravel()
z=c.ravel()

print(x)
print(y)
print(z)