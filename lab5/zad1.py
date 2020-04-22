
lista = []
for  n in range(0,100):
    if n % 4 == 0:
        lista +=[n]

plik = open("plik.txt","w+")

plik.writelines(str(lista))

plik.close()