# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:

# wyświetl_dane – drukuje elementy na ekran
# pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# policz_sume – liczy sume elementow
# policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.


class ciagi_arytmetyczne:
    def __init__(ciag, a1, r, n):
        ciag.a1 = a1
        ciag.r = r
        ciag.n = n
        
    def wyświetl_dane(dane):
        print("Pierszwszy wyraz ciagu: " + str(dane.a1) + "\n"
         + "Roznica: " + str(dane.r) + "\n"
        + "Ilosc elementow ciagu: " + str(dane.n))
    def pobierz_elementy(el):
        el.a1 = int(input("Podaj pierwszy wyraz ciagu: "))
        el.r=int(input("Podaj roznice ciagu: "))
        el.n=int(input("Podaj ilosc wyrazow ciagu: "))
    def policz_sume(suma):
        n_wyraz = suma.a1 + (suma.n - 1) * suma.r
        return ((suma.a1 + n_wyraz)/2)*suma.n
        
    def policz_elementy(licz):
        return licz.a1 + (licz.n - 1) * licz.r

    


p1 = ciagi_arytmetyczne(1, 2, 15)
p1.pobierz_elementy()
p1.wyświetl_dane()
print("Suma: " + str(p1.policz_sume()))
print("An: " + str(p1.policz_elementy()))

