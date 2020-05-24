# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
import numpy as np

def dodawanie(a,b):
    print(a+b)

a = np.array( [20,2,-76,1] )
b = np.arange(4)
dodawanie(a,b)