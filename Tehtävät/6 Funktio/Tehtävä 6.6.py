#Ympyrän pinta-ala= pii*r^2
def pinta_ala(pizzansade,pizzanhinta):
    area = 3.14*pizzansade**2
    metreiksi = area / 1000
    jako = pizzanhinta/metreiksi
    return jako

pizzansade= 20
pizzahinta= 8

pinta_ala(pizzansade,pizzahinta)
vastaus= pinta_ala(pizzansade,pizzahinta)

#print(f"{vastaus:0.2f} €/m2")

halkaisija1= int(input("Anna 1. halkaisija:"))
hinta1 = int(input("Anna 1.pizzan hinta:"))

halkaisija2=int(input("Anna 2. pizzan halkaisija:"))
hinta2 = int(input("Anna 2. pizzan hinta:"))

lopputulos1 = pinta_ala(halkaisija1, hinta1)
lopputulos2 = pinta_ala(halkaisija2, hinta2)

if lopputulos1 < lopputulos2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
elif lopputulos1 > lopputulos2:
    print("Toinen pizza antaa paremman vastineen rahalle")
else:
    print("Antavat saman vastineen rahalle")

