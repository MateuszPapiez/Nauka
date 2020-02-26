import requests
from OLX import OLXParser
from OTODOM import OTODOMParser

r = requests.get("https://www.olx.pl/nieruchomosci/mieszkania/wroclaw")
zr_strony=r.text
r2=requests.get("https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw")
zr2_strony=r2.text

#print(r.status_code)
#print(zr_strony)

olx_parser = OLXParser(zr_strony)
olx_parser.zbierz_informacje_o_mieszkaniach()
#oto_dom_parser=OTODOMParser(zr2_strony)
#oto_dom_parser.zbierz_informacje_o_mieszkaniach()
#oto_dom_parser.zapisz_plik()
olx_parser.zapisz_plik()



