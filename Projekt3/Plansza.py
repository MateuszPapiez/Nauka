class Plansza():

    def __init__(self,rozmiar_planszy):
        self.rozmiar_planszy=rozmiar_planszy
        self.plansza=self.generuj_plansze()




    def generuj_plansze(self):
        generuj=['-' for i in range(self.rozmiar_planszy)]
        lista=[]
        for i in range(self.rozmiar_planszy):
            lista.append(generuj.copy())    #copy jak coś zmienimy to nie ma efektu na wszystkie
        return lista

    def rysuj_plansze(self):
        for i,row in enumerate(self.plansza):
            print("{} {}".format(self.rozmiar_planszy-1-i," ".join(row)))
        print(" ",end="")
        for y in range(self.rozmiar_planszy):
            print(" {}".format(y), end="")
        print()

    def polozenie_klocka_na_planszy(self,y,x):

        #wyzerowanie_pozycji_klocka
        for row in self.plansza:                #dla row w liscie , dla i z zakresu znakow w row, jesli row [i] bedzie tam x (sprawdzamy) to row [i]= -
            for i in range(len(row)):
                if row[i]=="X":
                    row[i]="-"

        if y>4 or x>4:
            x=0
            y=0
        elif y<0 or x<0:
            y=0
            x=0



        #ustawianie klocka
        self.pozycja_y=self.rozmiar_planszy -1-y
        self.plansza[self.pozycja_y][x] = "X"






