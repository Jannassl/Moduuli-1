joukko = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in joukko:
        print("Aiemmin syötetty nimi")
    elif nimi not in joukko:
        print("Uusi nimi")

    joukko.add(nimi)

for n in joukko:
    print(n)


