# Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:

# sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
# sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
# sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
# wyświetl_wyrazy – wyświetla podane wyrazy
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class Slowa: 
    def __init__(abc, slowo1, slowo2):
        abc.slowo1 = slowo1
        abc.slowo2 = slowo2

    def sprawdz_czy_palindrom(pal):
        def reverse(s): 
            return s[::-1] 
        def isPalindrome(s): 
            rev = reverse(s) 
            if (s == rev): 
                return True
            return False
  
        s = pal.slowo1
        ans = isPalindrome(s) 
  
        if ans == 1: 
            print("Palindrom") 
        else: 
            print("Nie palindrom") 
    def sprawdz_czy_metagramy(abc):
        wynik = 0
        if (len(abc.slowo1) != len(abc.slowo2)):
            print("To nie metagram")
        else:
            for x in range(len(abc.slowo1)):
                if abc.slowo1[x] == abc.slowo2[x]:
                    wynik+=1
        if wynik == (len(abc.slowo1) - 1):
            print("Metagram")
        else:
            print("To nie jest metagram")
    def sprawdz_czy_anagramy(abc):
        if(sorted(abc.slowo1) == sorted(abc.slowo2)): 
            print("Anagram")  
        else: 
            print("To nie anagram.") 
    def wyświetl_wyrazy(abc):
        print(str(abc.slowo1 + " ; " + str(abc.slowo2)))

        

p1 = Slowa("kajak","mama")
p1.wyświetl_wyrazy()
p1.sprawdz_czy_palindrom()
p2 = Slowa("tama","mama")
p2.wyświetl_wyrazy()
p2.sprawdz_czy_metagramy()
p3 = Slowa("mata","tama")
p3.wyświetl_wyrazy()
p3.sprawdz_czy_anagramy()
