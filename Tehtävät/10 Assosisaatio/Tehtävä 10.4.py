import random
class Auto:
    def __init__(self,rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.nykyinen_matka = 0
    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeuden_muutos
        if uusi_nopeus <0:
            self.nykyinen_nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        else:
            self.nykyinen_nopeus = uusi_nopeus
        return

    def kulje(self,tunnit):
        self.nykyinen_matka += tunnit * self.nykyinen_nopeus
        return

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta()
            auto.kulje()


autot = []
auto = Auto


for i in range(10):
    rekisteritunnus = f"ABC-{i +1}"
    huippunopeus = random.randint(100,200)
    auto = Auto(rekisteritunnus,huippunopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli",8000,autot)
kilpailu.tulosta_tilanne()