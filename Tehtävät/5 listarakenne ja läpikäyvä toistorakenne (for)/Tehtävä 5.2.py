lista = []

while True:
    luku = input("Anna luku")
    if luku == "":
        break
    lista.append(int(luku))

lista.sort(reverse=True)
print(lista[0:4])

