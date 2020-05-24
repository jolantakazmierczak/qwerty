# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).

import numpy as np
import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt


df = pd.read_csv('zamowieniana.csv', sep=';')
grupa = df.groupby(['Sprzedawca']).agg({'idZamowienia':['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Ilosc')
wykres.set_xlabel('Sprzedawca')
wykres.legend()
plt.title('Llość złożonych zamówień przez poszczególnych sprzedawców z podziałem na kontynenty')
plt.show()