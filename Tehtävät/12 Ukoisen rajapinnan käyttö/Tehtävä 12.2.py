import requests
import json

api_key = "b2c9e5b457399add9ba4e91eec30b2ac"
url = "http://api.openweathermap.org/data/2.5/forecast?"
sijainti = input("Anna kaupunki: ")
valmis_url=url + "appid=" + api_key +"&q="+sijainti

vastaus = requests.get(valmis_url).json()

#print(json.dumps(vastaus, indent=2))

kuvaus = vastaus["list"][0]["weather"][0]["description"]
kelvins = vastaus["list"][0]["main"]["temp"]
celsius = kelvins- 273.15
print(vastaus["city"]["name"])
print(f"Celsius asteet: {celsius:.2f}C")
print(f"Sään kuvaus: {kuvaus}")



