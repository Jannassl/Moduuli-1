import random
def silmaluku(maksimi):


    while True:

        noppa = random.randint(1, maksimi)
        if noppa != maksimi:
            print(f"Silmäluku: {noppa}")
        else:
            break

maksimi = int(input("Anna maksimi:"))
silmaluku(maksimi)