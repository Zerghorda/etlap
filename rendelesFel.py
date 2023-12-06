def rendelesLeves(jel1, levesek, levesAr, jel2, etlap_hossz, rendelt, rendeltArak):
    rendeles = input("Szeretne e rendelni levest?(I/N)")
    if rendeles == "I" or rendeles == "i":
        folytat = True
        while folytat == True:
            valasztot = int(input("Adjon meg egy leves számát!(1-2)"))
            if valasztot == 1:
                rendelt.append(levesek[0])
                rendeltArak.append(levesAr[0])
            elif valasztot == 2:
                rendelt.append(levesek[1])
                rendeltArak.append(levesAr[1])
            else:
                print("Hibásan adta meg a választ!")
            kerdes = input("Szeretne többet rendelni?(I/N)")
            if kerdes == "N" or kerdes == "n":
                folytat = False
            else:
                print("Hibásan adta meg a választ!")
    elif rendeles == "n" or rendeles == "N":
        return
    else:
        print("Hibásan adta meg a választ!")


def rendelesFoetelek(jel1, foetelek, foetelAr, jel2, etlap_hossz, rendelt, rendeltArak):
    rendeles = input("Szeretne e rendelni főételt?(I/N)")
    if rendeles == "I" or rendeles == "i":
        folytat = True
        while folytat == True:
            valasztot = int(input("Adjon meg egy főétel számát!(1-2)"))
            if valasztot == 1:
                rendelt.append(foetelek[0])
                rendeltArak.append(foetelAr[0])
            elif valasztot == 2:
                rendelt.append(foetelek[1])
                rendeltArak.append(foetelAr[1])
            else:
                print("Hibásan adta meg a választ!")
            kerdes = input("Szeretne többet rendelni?(I/N)")
            if kerdes == "N" or kerdes == "n":
                folytat = False
            else:
                print("Hibásan adta meg a választ!")
    elif rendeles == "n" or rendeles == "N":
        return
    else:
        print("Hibásan adta meg a választ!")
