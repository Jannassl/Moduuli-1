kayttaja_oikein = "python"
salasana_oikein = "rules"
i = 0
while i <6:
    kayttaja = input("Anna käyttäjätunnus:")
    salasana = input("Anna salasana:")

    if kayttaja == kayttaja_oikein and salasana == salasana_oikein:
        print("Tervetuloa")
        break
    else:
        print("pääsy evätty")

    i+=1
