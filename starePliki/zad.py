# zad1
# zdanie = input("Podaj zdanie: \n")
# print(zdanie)
# print(zdanie.count(' '))

#zad2
# a = input("Podaj czynna: \n")
# b = input("Podaj czynnik: \n")
# wynik = int(a)*int(b)
# print("wynik: " + str(wynik))

#zad4
# a = input("Podaj liczbę: ")
# wynik=abs(int(a))
# print("wynik: " + str(wynik))

#zad5
# a = input("Podaj liczbę a: ")
# b = input("Podaj liczbę b: ")
# c = input("Podaj liczbę c: ")

# if 10>int(a)>0 & (int(a)>int(b) | int(b)>int(c)):
#     print("warunek spełniony")

# else:
#     print("warunek nie spełniony")  

#zad6
# lower=int(input("Enter lower range limit:"))
# upper=int(input("Enter upper range limit:"))
# n=int(input("Enter the number to be divided by:"))
# for i in range(lower,upper+1):
#     if(i%n==0):
#         print(i)

#zad7
# liczba = input("Podaj liczbę: ")
# for liczba in range(3):
#     print(liczba*liczba)

#zad8

# lista = []
# while(len(lista)<=4):
#     liczba = input("Podaj liczbę: ")
#     liczba = int(liczba)
#     lista.append(liczba)
# else:
#     print("Lista osiągnęła maksymalną długość")

# print(lista)

#zad9
# wynik = 0
# wynik = int(wynik)
# while():
#     liczba = input("Podaj liczbę: ")
#     liczba = int(liczba)
# dokończ

#zad10
# n = input("Podaj wysokość piramidy: ")
# n = int(n)
#  for i in range(0, n): 
      

#      for j in range(0, i+1): 
          

#          print("A ",end="") 
       

#      print("\r") 

#zad11
# h = eval(input("Podaj wysokość: "))

# for i in range(h):
#     print(" "*(h-i), "o"*(i*2+1))
# for i in range(h-2, -1, -1):
#     print(" "*(h-i), "o"*(i*2+1))

#zad12
liczba = input("Podaj liczbę: ")
try:
    wynik = math.sqrt(liczba)
    print("Wynik: "+ str(wynik))
     except ValueError:
         print("Błędnie podana liczba")

