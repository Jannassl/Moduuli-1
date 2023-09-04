airports = {"EFHK": "Helsinki-Vantaa airport",
               "EGLL": "Heathrow",
               "EGGP": "John Lennon airport"}

while True:
    valinta = input("Add(A),search(S) or quit(Q): ")
    if valinta =="Q":
        break
    elif valinta == "A":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna kentän nimi: ")
        airports[icao] = nimi
    elif valinta == "S":
        kysy_icao = input("Anna ICAO-koodi: ")
        print(airports[kysy_icao])
