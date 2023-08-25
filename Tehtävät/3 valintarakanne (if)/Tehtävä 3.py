
sukupuoli = input("Sukupuoli")
arvo = int(input("Hemoglobiini arvo"))

if sukupuoli == "nainen":
    if arvo > 175:
        print("korkea")
    if arvo > 117 and arvo <= 175:
        print("normaali")
    if arvo < 117:
        print("alhainen")


if sukupuoli == "mies":
    if arvo > 195:
        print("korkea")
    if arvo > 134 and arvo <= 195:
        print("normaali")
    if arvo < 134:
        print("alhainen")


