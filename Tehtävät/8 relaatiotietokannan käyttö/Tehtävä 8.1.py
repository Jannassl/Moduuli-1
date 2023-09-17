import mysql.connector

def ICAO_kodi(koodi):
    sql = 'SELECT airport.name,municipality,ident FROM airport'
    sql += ' WHERE ident ="'+ koodi+'"'
    #print(sql)

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"Lentokentän nimi: {rivi[0]} sijaintikunta: {rivi[1]}")

    return


#PÄÄOHJELMA

yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'Nasslingmaga98',
    autocommit = True
)
koodi = input("Anna ICAO-koodi: ")
ICAO_kodi(koodi)




