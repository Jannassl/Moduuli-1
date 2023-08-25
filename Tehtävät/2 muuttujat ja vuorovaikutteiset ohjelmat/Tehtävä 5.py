gramma = 1
luoti = gramma*13.3
naula = luoti*32
leiviska = naula*20



leiviskat = int(input("Anna leiviskat:"))
naulat = int(input("Anna naulat:"))
luodit = float(input("Anna luodit"))



summa = (leiviskat * leiviska)+ (naulat*naula)+(luoti*luodit)
kg = int(summa//1000)
g = float(round(summa%1000,2))

print("Massa nykymittojen mukaan:")
print(f"{kg} kilogrammaa ja {g} grammaa.")
