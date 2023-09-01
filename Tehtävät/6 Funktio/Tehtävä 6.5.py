def parilliset(luvut):
    parilliset_luvut= []
    for n in luvut:
        if n %2 == 0:
            parilliset_luvut.append(n)
    return parilliset_luvut



luvut = [1,2,3,4,5,6,7,8,9,10]

parilliset(luvut)

vastaus = parilliset(luvut)

print(luvut)
print(vastaus)