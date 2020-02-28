import random

def pobierz_dane():
    liczba=input("podaj liczbe: ")
    return liczba
def losuj_liczbe():
    #liczba=str(1114)
    liczba=str(random.randint(1000,9999))
    return liczba
def wylicz_krowy(liczba_uzytkownika,liczba_wylosowana):
    krowy = 0
    for i in range(len(liczba_uzytkownika)):
       if liczba_uzytkownika[i]==liczba_wylosowana[i]:
        krowy+=1
    return krowy
#
def wylicz_byki(liczba_uzytkownika,liczba_wylosowana):
    byki=0
    for i in range(len(liczba_uzytkownika)):
        if liczba_uzytkownika[i]!=liczba_wylosowana[i] and liczba_uzytkownika[i] in liczba_wylosowana:
                byki+=1
        #if liczba_uzytkownika[i] in liczba_wylosowana and liczba_uzytkownika[i] != liczba_wylosowana[i]:
                #byki += 1
    return byki

liczba_wylosowana=losuj_liczbe()
print(liczba_wylosowana)
podejscia=0
while True:
    liczba_uzytkownika = pobierz_dane()
    podejscia+=1
    if liczba_uzytkownika==liczba_wylosowana:
        print("koniec gry")
        print("podejscia:{}".format(podejscia))
        break
    else:
        krowy=wylicz_krowy(liczba_uzytkownika,liczba_wylosowana)
        print(krowy)
        byki=wylicz_byki(liczba_uzytkownika,liczba_wylosowana)
        print(byki)
        print("Krowy:{},Byki:{}".format(krowy,byki))
        print("podejscia:{}".format(podejscia))



#wylosowanie liczby przez komputer
#pobranie liczby od uzytkownika
#sprawdzenie czy liczba wylosowana jest równa liczbie uzytkownika
#jeśli sarówne informujemy o końcu gry
#jeśli nie to
    #wyliczamy liczbe krów
    #wyliczamy liczbe byków
#informacje odnoślie liczby krów i byków
#zliczenie prób

