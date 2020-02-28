
class Ruch():
    def __init__(self):
        self.y = 0
        self.x = 0
        self.kat = 0

    def przeksztalcenie_ruchu(self,ruch_uzytkownika):

        for self.znak in ruch_uzytkownika:
            if self.znak == "M":
                if self.kat==0:
                    self.y+=1
                elif self.kat ==90:
                    self.x+=1
                elif self.kat==180:
                    self.y-=1
                elif self.kat==270:
                    self.x-=1
            elif self.znak=="R":
                self.kat+=90
                if self.kat >=360:
                    self.kat=0
            elif self.znak=="L":
                self.kat-=90
                if self.kat<=-360:
                    self.kat=0
        return self.x,self.y

















