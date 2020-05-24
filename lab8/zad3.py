# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:

# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# 5 najwyższych wartości zamówień
# ilość zamówień złożonych przez każdego sprzedawcę
# sumę zamówień dla każdego kraju
# sumę zamówień dla roku 2005, dla sprzedawców z Polski
# średnią kwotę zamówienia w 2004 roku,
# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv

import numpy as np
import pandas as pd
import xlrd
import openpyxl


df = pd.read_csv('zamowieniana.csv', sep=';')
print(df)