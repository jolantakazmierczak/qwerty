# imie = "JOLANTA"
# nazwisko = "KAZMIERCZAK"
# print(imie.capitalize() + ' ' + nazwisko.capitalize())


# def funkcka():
#     print(imie.capitalize() + ' ' + nazwisko.capitalize())
print("Ala ma " +  " kota") #konkatenacja
print(0 - 1)
print(2 / 1)
print(2 * 1)
print(2 // 1) #dzielenie bez reszty
print(2 ** 1) #potęgowanie
print(2 % 1) #dzielenie modulo
print("Ala ma 5 lat")
print("Ala ma " +  str(5) + " lat")
print("Ala ma {} lat".format(5))
print("Ala ma {1} lat a Marta {0}".format(5, 10))
#f-string
wiek = 5
print(f"Ala ma {wiek} lat")


imie = "Małgorzata"
print(imie[3])
imie = "Adam"
imie.lower()
print(imie)
print(imie.lower())
"Wojtek".lower().lstrip().rstrip()


#listy

lista = []
print(type(lista))
print(type("Ala"))
print(type(5))

# <class 'list'>
# <class 'str'>
# <class 'int'>

lista.append(5)
lista.insert(0, 6)
lista2 = [1, 2, 3, 4, 5]
lista2[2]
lista3 = lista + lista2
print(lista3)
lista4 = [1, "Ala", imie, 3.4, [1, 3]]
print(lista4[4][1])

macierz=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(macierz[1][1])

#słownik
slownik = {}
print(type(slownik))
# <class 'dict'>
slownik["imie"] = "Marek"
print(slownik)
slownik2 = {
    'imie': 'Marek',
    'wiek': 25,
    'wzrost': 182}

#  print(slownik2)
#  print(slownik2.items())
#  print(slownik2.keys())
#  print(slownik2['imie'])

def pow(): 
    pass


#import
# from math import *
# from math import pow  #niezalecane

import math as m

print(m.pow(2, 10
))

