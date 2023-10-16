class Auto:
    def __init__(self,rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

uusi_auto = Auto("ABC-123", 142)

print("Rekisteritunnus:",uusi_auto.rekisteritunnus)
print("Huippunopeus:", uusi_auto.huippunopeus,"Km/h")
print("Nopeus:", uusi_auto.nopeus,"Km/h")
print("Kuljettu matka:", uusi_auto.matka, "Km")

