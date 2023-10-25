class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivumaara: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self,nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja
    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Päätoimittaja: {self.paatoimittaja}")

julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for j in julkaisut:
    j.tulosta_tiedot()