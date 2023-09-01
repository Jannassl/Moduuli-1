vuodenajat = ("Tammikuu", "Helmikuu","Maaliskuu", "Huhtikuu", "Toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu","joulukuu")

luku = int(input("Anna kuukauden numero(1-12): "))

vuodenaika = vuodenajat[luku-1]


if luku == 12 or luku == 1 or luku ==2:
    print("Talvi")
elif luku < 6:
    print("Kevät")
elif luku < 9:
    print("Kesä")
elif luku < 12:
    print("Syksy")
elif luku > 12:
    print("Ei ollut 1-12 välissä")