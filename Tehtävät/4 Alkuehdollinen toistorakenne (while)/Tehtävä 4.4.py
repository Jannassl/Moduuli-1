import random

while True:
    luku = int(input("Anna luku:"))
    arpa = random.randint(1,10)
    print(luku)
    print(arpa)
    if luku == arpa:
        print("oikein.")
        break
    elif luku < arpa:
        print("Liian pieni arvaus")
    elif luku > arpa:
        print("Liian suuri arvaus")


