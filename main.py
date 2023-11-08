asztalok = []
foglalasok = []

def asztal_betoltes():
    with open('assets/asztalok.txt', 'r') as file:
        for line in file:
            data = line.strip().split(";")
            azonosito, szekek, hely = int(data[0]), int(data[1]), data[2]
            asztalok.append({"azonosito": azonosito, "szekek": szekek, "hely": hely})


def foglalas():
    nev = input("Vendég neve: ")
    kezdete = input("Foglalás kezdete (HÓNAP-NAP ÓRA:PERC formátumban): ")
    vege = input("Foglalás vége (ÓRA:PERC formátumban): ")
    szekek = input("Foglalt székek száma: ")
    hely = input("Beltéri vagy kültéri asztalt szeretnének (B = beltéri, K = kültéri): ")


def torles():
    print("Foglalás törlése")


def statisztika():
    print("Statisztika")


def main():
    asztal_betoltes()

    print("\nMenü:")
    print("1. Foglalás")
    print("2. Foglalás törlése")
    print("3. Statisztika")
    print("4. Kilépés\n")

    while True:
        opciok = input("1/2/3/4: ")
        if opciok == "1":
            foglalas()
        elif opciok == "2":
            torles()
        elif opciok == "3":
            statisztika()
        elif opciok == "4":
            print("Kilépés!")
        else:
            continue
        break


if __name__ == "__main__":
    main()
