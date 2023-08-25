raja = 37

pituus = int(input("Kuhan pituus:"))

if pituus < 37:
    erotus = raja - pituus
    print(f"Laske kuha takaisin järveen. Pituutta puuttuu {erotus}cm")
else:
    print("Onnea")