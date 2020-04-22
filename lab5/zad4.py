# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:

# nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
# konstruktor – który nadaje wartości
# wyświetl_produkt() – drukuje informacje o produkcie na ekranie
# ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2
class NaZakupy:
    def __init__(kup, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        kup.nazwa_produktu = nazwa_produktu
        kup.ilosc = ilosc
        kup.jednostka_miary = jednostka_miary
        kup.cena_jed = cena_jed
    
    def wyświetl_produkt(abc):
        print("Kup: " + abc.nazwa_produktu)

    def ile_produktu(xyz):
        print("Ile: " + str(xyz.ilosc) + " " + xyz.jednostka_miary)

    def ile_kosztuje(koszt):
        return koszt.ilosc * koszt.cena_jed
    

p1 = NaZakupy("marchew", 3, "kg", 1.5)
p1.wyświetl_produkt()
p1.ile_produktu()
print("Cena: " + str(p1.ile_kosztuje()) + " zł")