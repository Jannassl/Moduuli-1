class Auto:
    def __init__(self,rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 50
        self.matka = 0
    def kulje(self,aika):
        self.aika = aika
        self.matka = (self.nopeus *aika)

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus,huippunopeus)

        self.akkukapasiteetti = akkukapasiteetti
    def tulosta_tiedot(self):
        print(f"Rekkari: {self.rekisteritunnus}, Matkamittarilukema: {self.matka}")
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_tilavuus):
        super().__init__(rekisteritunnus,huippunopeus)

        self.bensatankin_tilavuus = bensatankin_tilavuus
    def tulosta_tiedot(self):
        print(f"Rekkari: {self.rekisteritunnus}, Matkamittarilukema: {self.matka}")

autot = []

autot.append(Sähköauto("ABC-15",180, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))

for a in autot:
    a.kulje(3)
    a.tulosta_tiedot()