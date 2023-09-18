import mysql.connector
from geopy.distance import geodesic

def kenttien_etaisyys(kentta1,kentta2):
    sql = "select airport.longitude_deg, airport.latitude_deg from airport where ident='"+kentta1+"'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos1 = kursori.fetchall()
    #print(tulos1)

    sql2 = "select airport.longitude_deg, airport.latitude_deg from airport where ident='"+kentta2+"'"
    kursori = yhteys.cursor()
    kursori.execute(sql2)
    tulos2 = kursori.fetchall()
    #print(tulos2)

    sijainti1 = (tulos1['longitude_deg'], tulos1['latitude_deg'])
    sijainti2 = (tulos2['longitude_deg'], tulos2['latitude_deg'])

    vastaus = geodesic(sijainti1,sijainti2).kilometers
    print(f"Etäisyys on {vastaus} kilometriä")
    return

yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'Nasslingmaga98',
    autocommit = True
)

kentta1 = input("Anna ensimmäinen lentokenttä: ")
kentta2 = input("Anna toinen lentokenttä: ")

kenttien_etaisyys(kentta1,kentta2)