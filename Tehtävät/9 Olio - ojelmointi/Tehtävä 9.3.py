
class Auto:
    def __init__(self,rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 60
        self.nykyinen_matka = 2000
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



uusi_auto = Auto("ABC-123", 142)
uusi_auto.kulje(1.5)
print("Rekisteritunnus:",uusi_auto.rekisteritunnus)
print("Huippunopeus:", uusi_auto.huippunopeus,"Km/h")
print("Nopeus:", uusi_auto.nykyinen_nopeus,"Km/h")
print("Kuljettu matka:", uusi_auto.nykyinen_matka, "Km")

