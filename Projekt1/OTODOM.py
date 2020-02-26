from bs4 import BeautifulSoup
#import csv
#import pandas

class OTODOMParser():

    def __init__(self,text_html):
        self.soup_html = BeautifulSoup(text_html)
        self.wszystkie_mieszkzania = self.wyszukaj_mieszkania()
        self.dane=[]


    def wyszukaj_mieszkania(self):
        mieszkanie=self.soup_html.findAll('div', {
            'class': 'offer-item-details'})
        return mieszkanie


    def wyszukaj_tytul(self,mieszkanie):
        tytul=mieszkanie.find('span', {'class': 'offer-item-title'}).getText()
        return tytul.encode('utf=8')

    def wyszukaj_link(self,mieszkanie):
        link=mieszkanie.find("a")
        return link["href"].replace(" ","").encode('utf=8')

    def cena_mieszkania(self,mieszkanie):
        cena=mieszkanie.find('li',{'class':'offer-item-price'}).get_text()
        return cena.replace(" ","").encode('utf=8')

    def powierzchnia(self,mieszkanie):
        powierzchnia_mieszkania=mieszkanie.find('li',{'class':'hidden-xs offer-item-area'}).getText()
        return powierzchnia_mieszkania.replace(" ","").encode('utf=8')

    def dzielnica(self,mieszkanie):
        lokalizacja=mieszkanie.find('span').get_text()
        return lokalizacja.encode('utf=8')

    def zbierz_informacje_o_mieszkaniach(self):
        for mieszkanie in self.wszystkie_mieszkzania:
            #print(mieszkanie)
            tytul=self.wyszukaj_tytul(mieszkanie)
            #print(tytul)
            cena=self.cena_mieszkania(mieszkanie)
            #print(cena)
            link=self.wyszukaj_link(mieszkanie)
            #print(link)
            powierzchnia_mieszkania=self.powierzchnia(mieszkanie)
            #print(powierzchnia_mieszkania)
            lokalizacja=self.dzielnica(mieszkanie)
            #print(lokalizacja)
            self.dane.append("{},{},{},{},{}".format(tytul,link,cena,powierzchnia_mieszkania,lokalizacja))


    def zapisz_plik(self):
        print(self.dane)
        with open("otodom.csv", 'w') as f:
            for mieszkanie in self.dane:
                #print(mieszkanie)
                f.write("{}\n".format(mieszkanie))




