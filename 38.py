#!/usr/bin/env python3
import numpy as np
mozi = np.full((40,100), 'X')


def foglalas():
    mg = input("adja meg monogrammjat: ")
    sor = input("adja meg a foglalni kivánt sort: ")
    szek = input("adja meg a foglalni kivant szeket: ")
    sor = int(sor)
    szek = int(szek)
    if mozi[sor][szek * 2] != 'X':
        print("ez a hely foglalt! Válasszon másikat")
    else:
        mozi[sor][szek * 2] = mg[0]
        mozi[sor][szek * 2 + 1] = mg[1]
        print (mozi)
    return mozi


def kereses():
    mg = input("adja meg monogrammjat: ")
    vnev=mg[0]
    knev=mg[1]
    for i in range(40):
        for j in range(100):
            if mozi[i][j//2] == vnev and mozi[i][j//2+1] == knev:
                    print(i, "sor", (j//4), "szek")




def modositas():
    mg=input("adja meg monogrammajat: ")
    sor = input("adja meg a foglalni kivánt sort: ")
    szek = input("adja meg a foglalni kivant szeket: ")
    sor = int(sor)
    szek = int(szek)
    vnev=mg[0]
    knev=mg[1]
    for i in range(40):
        for j in range(100):
            if mozi[i][j // 2] == vnev and mozi[i][j // 2 + 1] == knev:
                mozi[i][j // 2] ='X'
                mozi[i][j // 2 + 1] = 'X'
                if mozi[sor][szek * 2] != 'X':
                    print("ez a hely foglalt! Válasszon másikat")
                else:
                    mozi[sor][szek * 2] = mg[0]
                    mozi[sor][szek * 2 + 1] = mg[1]
                    print("a modositas sikeres")





                return None




def torles():
    mg = input("adja meg monogrammjat: ")
    vnev = mg[0]
    knev = mg[1]
    for i in range(40):
        for j in range(100):
            if mozi[i][j // 2] == vnev and mozi[i][j // 2 + 1] == knev:
                mozi[i][j // 2] ='X'
                mozi[i][j // 2 + 1] ='X'
                print("torles sikeres")




    return None



def main():
    utasitas = input("Adjon meg egy utasítást (foglalas/kereses/modositas/torles/helyek): ")
    while utasitas != "END":
        if utasitas == "foglalas":
            foglalas()
        elif utasitas == "kereses":
            kereses()
        elif utasitas == "modositas":
            modositas()
        elif utasitas == "torles":
            torles()
        elif utasitas == "helyek":
            for j in mozi:
                print(j)
        else:
            print("Nincs ilyen utasítás!")
        utasitas = input("Adjon meg egy utasítást: (foglalas/kereses/modositas/torles): ")


if __name__ == "__main__":
    main()
print(mozi)
