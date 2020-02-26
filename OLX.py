from bs4 import BeautifulSoup

class OLXParser():

    def __init__(self,text_html):
        self.soup_html = BeautifulSoup(text_html)
        self.wszystkie_mieszkzania=self.wyszukaj_mieszkania()
        self.dane=[]

    def wyszukaj_mieszkania(self):
        mieszkania= self.soup_html.findAll('div', {
            'class': 'offer-wrapper'})                                  # szukamy kluczy div o atrybucie Class którego wartosc to offer...
        return mieszkania

    def wyszukaj_tytul(self,mieszkanie):
        tytul=mieszkanie.find('strong').get_text("strong")
        return tytul

    def wyszukaj_link(self,mieszkanie):
        link=mieszkanie.find("a")
        return link['href'].replace(" ","").replace("\n","").encode('utf=8')

    def cena_mieszkania(self,mieszkanie):
        cena=mieszkanie.find("p",{'class':'price'})
        if cena:
            cena=cena.get_text().replace(" ","").replace("\n","")
        return cena

    def sprzedaz_wynajem(self,mieszkanie):
        sprzedaz_lub_wynajem=mieszkanie.find('small', {'class': 'breadcrumb x-normal'}).getText()
        return sprzedaz_lub_wynajem.replace(" ","").replace("\n","")
###########################################################################################################
    def lokalizacja(self,mieszkanie):
        dzielnica=mieszkanie.find('span').get_text()
        return dzielnica.replace(" ","").replace("\n","")
    def do_negocjacji(self,mieszkanie):
        negocjacje=mieszkanie.find('span', {'class': 'normal inlblk pdingtop5 lheight16 color-2'})
        if negocjacje:
            cena = negocjacje.getText().replace(" ","").replace("\n","")
        else:
            cena = "BRAK NEGOCJACJI"
        return cena


    def zbierz_informacje_o_mieszkaniach(self):
        for mieszkanie in self.wszystkie_mieszkzania:
            #print(mieszkanie)
            tytul=self.wyszukaj_tytul(mieszkanie)
            print(tytul)
            link=self.wyszukaj_link(mieszkanie)
            print(link)
            #print(mieszkanie)
            cena=self.cena_mieszkania(mieszkanie)
            print(cena)
            sprzedaz_lub_wynajem=self.sprzedaz_wynajem(mieszkanie)
            print(sprzedaz_lub_wynajem)
            dzielnica=self.lokalizacja(mieszkanie)
            print(dzielnica)
            negocjacje=self.do_negocjacji(mieszkanie)
            print(negocjacje)
            self.dane.append("{},{},{},{},{}".format(tytul,link,cena,sprzedaz_lub_wynajem,dzielnica,negocjacje))

    def zapisz_plik(self):
        print(self.dane)
        with open("olx.csv", 'w') as f:
            for mieszkanie in self.dane:
                f.write("{}\n".format(mieszkanie))

#olx dokonczyc
#krowki
