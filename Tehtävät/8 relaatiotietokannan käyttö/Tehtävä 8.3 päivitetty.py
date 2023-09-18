import mysql.connector
from geopy.distance import geodesic

def kenttien_etaisyys(kentta1, kentta2):
    sql = "SELECT airport.longitude_deg, airport.latitude_deg FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (kentta1,))
    tulos1 = kursori.fetchall()

    sql2 = "SELECT airport.longitude_deg, airport.latitude_deg FROM airport WHERE ident = %s"
    kursori.execute(sql2, (kentta2,))
    tulos2 = kursori.fetchall()

    ensimmainen_rivi_tulos1 = tulos1[0]
    longitude1 = ensimmainen_rivi_tulos1[0]
    latitude1 = ensimmainen_rivi_tulos1[1]

    ensimmainen_rivi_tulos2 = tulos2[0]
    longitude2 = ensimmainen_rivi_tulos2[0]
    latitude2 = ensimmainen_rivi_tulos2[1]

    sijainti1 = (longitude1, latitude1)
    sijainti2 = (longitude2, latitude2)

    vastaus = round(geodesic(sijainti1, sijainti2).kilometers, 2)
    print(f"Etäisyys on {vastaus} kilometriä")
    return

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='Nasslingmaga98',
    autocommit=True
)

kentta1 = input("Anna ensimmäinen lentokenttä: ")
kentta2 = input("Anna toinen lentokenttä: ")

kenttien_etaisyys(kentta1, kentta2)
