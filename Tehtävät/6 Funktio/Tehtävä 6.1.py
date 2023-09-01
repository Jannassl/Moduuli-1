import random
def silmaluku():


    while True:
        noppa = random.randint(1, 6)
        if noppa !=6:
            print(f"Silmäluku: {noppa}")
        else:
            break

silmaluku()
