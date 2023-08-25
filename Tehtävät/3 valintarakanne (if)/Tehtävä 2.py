lux = "LUX on parvekkeellinen hytti yläkannella."
a = "A on ikkunallinen hytti autokannen yläpuolella."
b = "B on ikkunaton hytti autokannen yläpuolella."
c = "C on ikkunaton hytti autokannen alapuolella."

hytti = input("Syötä hyttiluokka:")

if hytti == "LUX":
    print(lux)
elif hytti == "A":
    print(a)
elif hytti == "B":
    print(b)
elif hytti == "C":
    print(c)
else:
    print("Virheellinen hyttiluokka.")