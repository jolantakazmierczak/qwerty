# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):

# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# tylko rekordy gdzie nadane imię jest takie jak Twoje
# sumę wszystkich urodzonych dzieci w całym danym okresie,
# sumę dzieci urodzonych w latach 2000-2005
# sumę urodzonych chłopców i dziewczynek,
# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,

import numpy as np
import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')


print(df[df['Liczba']>1000])
print(df[df['Imie']=='JOLANTA'])
print(df['Liczba'].sum())
print(df.loc[df['Rok']<2006, 'Liczba'].sum())
print(df.groupby(df['Plec']).agg({'Liczba':['sum']}))
print(df.sort_values('Liczba', ascending=False).groupby(['Rok','Plec']).nth(0))
print(df.sort_values('Liczba', ascending=False).groupby(['Plec']).nth(0))