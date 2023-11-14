import mysql.connector
from flask import Flask, request
app = Flask(__name__)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Nasslingmaga98',
         autocommit=True
         )
@app.route('/kenttä/<icao>')
def kenttä(icao):
    sql = "SELECT airport.ident, airport.name, municipality FROM airport"
    sql +=" INNER JOIN country ON country.iso_country = airport.iso_country"
    sql +=" WHERE airport.ident='"+icao+"'"
    arvot = []
    sanakirja = {

    }
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    i = 0
    arvot = []
    for rivi in tulos:
        while i < 3:
            arvot.append(rivi[i])
            i+=1
    #print(arvot)
    sanakirja["ICAO"]= arvot[0]
    sanakirja["Name"]= arvot[1]
    sanakirja["Municipality"] = arvot[2]
    return sanakirja

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)