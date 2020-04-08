
def monotonicznosc(y ,x ,b):
    a = (y-b)/x
    if (a > 0):
        print("Funkcja rosnaca")
    elif (a < 0):
        print("Funkcja malejaca")
    else:
         print("Funkcja stała")

monotonicznosc(4,2,2)


