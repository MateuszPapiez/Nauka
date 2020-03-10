
instrukcja=["1","2","3",
            "4","5","6",
            "7","8","9"]


plansza = ["-","-","-",
           "-","-","-",
           "-","-","-"]

gra_start = True
gracz = "X"
zwyciezca = None

def instrukcja_planszy():
    print("         Witaj w grze")
    print("         INSTRUKCJA")
    print("Cyfra odpowiada położeniu X lub O")
    print(instrukcja[0] + " | " + instrukcja[1] + " | " + instrukcja[2])
    print(instrukcja[3] + " | " + instrukcja[4] + " | " + instrukcja[5])
    print(instrukcja[6] + " | " + instrukcja[7] + " | " + instrukcja[8])


def start_gry():
    instrukcja_planszy()
    rysuj_plansze()

    while gra_start:

        wybierz_ruch(gracz)
        ruch_zakanczajacy_gre()
        wybor_gracz()

    if zwyciezca == "X" or zwyciezca == "O":
        print(zwyciezca + " wygrales")

    elif zwyciezca == None:
        print("Nikt nie wygrał-remis")

def rysuj_plansze():
    print("\n")
    print(plansza[0] + " | " + plansza[1] + " | " + plansza[2]+"     1 | 2 | 3")
    print(plansza[3] + " | " + plansza[4] + " | " + plansza[5]+"     4 | 5 | 6")
    print(plansza[6] + " | " + plansza[7] + " | " + plansza[8]+"     7 | 8 | 9")
    #print("\n")

def wybierz_ruch(osoba):
    print(osoba + " tura.")
    pozycja = input("Wybierz ruch 1-9: ")
    warunek = False
    while not warunek:
        while pozycja not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pozycja = input("Podaj ruch 1-9: ")

        pozycja = int(pozycja) - 1

        if plansza[pozycja] == "-":
            warunek = True
        else:
            print("Podaj ruch jeszcze raz")

    plansza[pozycja] = osoba
    rysuj_plansze()

def ruch_zakanczajacy_gre():
    sprawdz_ruch_wygrana()
    sprawdz_kwadrat()

def sprawdz_ruch_wygrana():
    global zwyciezca
    wygrana_w_rzedzie = ulozenie_w_rzedzie()

    wygrana_w_pionie = ulozenie_w_pionie()

    wygrana_w_ukos = ulozenie_w_ukos()

    if wygrana_w_rzedzie:
        zwyciezca = wygrana_w_rzedzie
    elif wygrana_w_pionie:
        zwyciezca=wygrana_w_pionie
    elif wygrana_w_ukos:
        zwyciezca= wygrana_w_ukos
    else:
        zwyciezca = None


def ulozenie_w_rzedzie():
    global gra_start
    rzad1=plansza[0]==plansza[1]==plansza[2] !="-"
    rzad2=plansza[3]==plansza[4]==plansza[5] !="-"
    rzad3=plansza[6]==plansza[7]==plansza[8] !="-"
    if rzad1 or rzad2 or rzad3:
        gra_start = False
    if rzad1:
        return plansza[0]
    elif rzad2:
        return plansza[3]
    elif rzad3:
        return plansza[6]
    else:
        return None

def ulozenie_w_pionie():
    global gra_start
    pion1 = plansza[0] == plansza[3] == plansza[6] !="-"
    pion2 = plansza[1] == plansza[4] == plansza[7] !="-"
    pion3 = plansza[2] == plansza[5] == plansza[8] !="-"
    if pion1 or pion2 or pion3:
        gra_start = False
    if pion1:
        return plansza[0]
    elif pion2:
        return plansza[1]
    elif pion3:
        return plansza[2]
    else:
        return None

def ulozenie_w_ukos():
    global gra_start
    ukos1 = plansza[0] == plansza[4] == plansza[8] !="-"
    ukos2 = plansza[2] == plansza[4] == plansza[6] !="-"
    if ukos1 or ukos2:
        gra_start = False
    if ukos1:
        return plansza[0]
    elif ukos2:
        return plansza[2]
    else:
        return None

def sprawdz_kwadrat():
    global gra_start
    if "-" not in plansza:
        gra_start = False
        return True
    else:
        return False
def wybor_gracz():
    global gracz
    if gracz=="X":
        gracz="O"
    elif gracz=="O":
        gracz="X"
    return

start_gry()

