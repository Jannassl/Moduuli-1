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


autot = []
auto = Auto


for i in range(10):
    rekisteritunnus = f"ABC-{i +1}"
    huippunopeus = random.randint(100,200)
    auto = Auto(rekisteritunnus,huippunopeus)
    autot.append(auto)

while auto.nykyinen_matka <= 10000:
    for auto in autot:
        auto.kiihdyta(random.randint(-10,15))
        auto.kulje(1)
        if auto.nykyinen_matka > 10000:
            print(f"VOITTAJA: {auto.rekisteritunnus},Huippunopeus: {auto.huippunopeus}, Nopeus: {auto.nykyinen_nopeus}. Kuljettu matka: {auto.nykyinen_matka}")
            break
        print(f"{auto.rekisteritunnus},Huippunopeus: {auto.huippunopeus}, Nopeus: {auto.nykyinen_nopeus}. Kuljettu matka: {auto.nykyinen_matka}")

