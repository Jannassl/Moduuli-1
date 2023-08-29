import random

kuutiot = int(input("Noppien määrä"))
lista = []

for noppa in range(kuutiot):
    noppa = random.randint(1, 6)
    lista.append(noppa)

print(sum(lista))