lista = []
while True:
    luku = input("Anna luku:")

    if luku =="":
        break
    lista.append(int(luku))

print(max(lista))
print(min(lista))