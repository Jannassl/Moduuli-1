def polttoaine(gallons):
    litrat = gallons*3.785
    return litrat

gallons = int(input("Gallons: "))

vastaus = polttoaine(gallons)
print(vastaus)