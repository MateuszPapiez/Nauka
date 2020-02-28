from Plansza import Plansza
from Ruch import Ruch

print("Witamy w grze")
plansza = Plansza(5)
licznik=0
plansza.polozenie_klocka_na_planszy(0,0)
ruch=Ruch()
while licznik<10:


    plansza.rysuj_plansze()
    #print("Aktualna pozycja klocka: 0,0")
    #pytanie_y=input("Podaj wspolzedna  Y: ")
    #pytanie_x=input("Podaj wspolzedna  X: ")
    #print(pytanie_y)
    #print(pytanie_x)

    #plansza.polozenie_klocka_na_planszy(4,4)
    #plansza.rysuj_plansze()
    #lokalizacja_y=int(pytanie_y)
    #lokalizacja_x=int(pytanie_x)
    ruch_uzytkownika=input("Podaj ruch: ")
    lokalizacja_x,lokalizacja_y=ruch.przeksztalcenie_ruchu(ruch_uzytkownika)
    print(lokalizacja_x,lokalizacja_y)
    plansza.polozenie_klocka_na_planszy(lokalizacja_y,lokalizacja_x)
    licznik+=1


