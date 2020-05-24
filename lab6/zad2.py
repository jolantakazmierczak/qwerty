# Stwórz listę składającą się z wartości zmiennoprzecinkowych 
# a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64.

import numpy as np

a = np.arange(2.1, dtype='float')
print(a.dtype)
b = a.astype('int64')
print(b.dtype)