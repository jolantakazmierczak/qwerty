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
    

    def __del__(kup):
        print("delete",kup.nazwa_produktu
    

p1 = NaZakupy("marchew", 3, "kg", 1.5)
p1.wyświetl_produkt()
p1.ile_produktu()
print("Cena: " + str(p1.ile_kosztuje()) + " zł")
 