# Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla Robaczka),
#  i powinna mieć następujące metody:

# konstruktor – który nadaje wartość dla x, y i krok
# idz_w_gore(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_dol(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_lewo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_prawo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne Robaczka
# Stwórz instancję klasy i sprawdź jak działają wszystkie metody



class Robaczek:

    def __init__(self, x, y, krok):
        self.x=x
        self.y=y
        self.krok=krok

    def idz_w_gore(self, ilosc):
        self.y+=ilosc*self.krok

    def idz_w_dol(self, ilosc):
        self.y-=ilosc*self.krok

    def idz_w_prawa(self, ilosc):
        self.x+=ilosc*self.krok

    def idz_w_lewa(self, ilosc):
        self.x-=ilosc*self.krok

    def pokaz_gdzie_jestes(self):
        return "x: "+str(self.x)+"; y: "+str(self.y)
robak=Robaczek(0, 0, 2)
print(robak.pokaz_gdzie_jestes())
robak.idz_w_gore(3)
robak.idz_w_dol(1)
robak.idz_w_prawa(4)
robak.idz_w_lewa(3)
print(robak.pokaz_gdzie_jestes())
del robak