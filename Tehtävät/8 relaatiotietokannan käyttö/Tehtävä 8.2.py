import mysql.connector

closed_list = []
small_list = []
medium_list = []
large_list = []
heliport_list = []
yhteensa = []
def maakoodi(koodi):
    koodi = koodi.upper()

    sql = "SELECT airport.type FROM airport, country"
    sql += " WHERE airport.iso_country = country.iso_country"
    sql += " and airport.iso_country ='"+koodi+"'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        #print(tulos)
        for rivi in tulos:
            yhteensa.append(rivi)
            if str(rivi) == "('closed',)":
                closed_list.append(rivi)
            elif str(rivi) == "('small_airport',)":
                small_list.append(rivi)
            elif str(rivi) == "('medium_airport',)":
                medium_list.append(rivi)
            elif str(rivi) == "('large_airport',)":
                large_list.append(rivi)
            elif str(rivi) == "('heliport',)":
                heliport_list.append(rivi)


    #print(sanat)


    return

yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'Nasslingmaga98',
    autocommit = True
)

koodi = input("Anna maakoodi: ")
maakoodi(koodi)
#print(len(closed_list))
#print(len(small_list))
#print(len(medium_list))
#print(len(large_list))
#print(len(heliport_list))
print(f"Lentokenttiä yhteensä: {len(yhteensa)}")
print(f"Suljettuja lentokenttiä: {len(closed_list)}")
print(f"Pieniä lentokenttiä: {len(small_list)}")
print(f"Keskikokoisia lentokenttiä: {len(medium_list)}")
print(f"Suuria lentokenttiä {len(large_list)}")
print(f"Helikopterien laskeutumisalustoja: {len(heliport_list)}")
