# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.


with open('zad3.txt', 'w+') as plik: 
    plik.write("Hello world !\n")
    plik.write("Witaj świecie  !\n")
    plik.write("Hallo Welt !\n")       


with open("zad3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")