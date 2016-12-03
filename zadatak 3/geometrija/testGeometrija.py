# -*- coding: utf-8 -*-

from geometrija import *

def main():
    x1 = input("Unesite x koordinatu za pocetnu tacku: ")
    y1 = input("Unesite y koordinatu za pocetnu tacku: ")
    x2 = input("Unesite x koordinatu za krajnu tacku: ")
    y2 = input("Unesite y koordinatu za krajnu tacku: ")

    tacka1 = Tacka(x1, y1)
    tacka2 = Tacka(x2, y2)
    duz1 = Duz.duz(tacka1, tacka2)

    x3 = input("Unesite x koordinatu za pocetnu tacku duži: ")
    y3 = input("Unesite y koordinatu za pocetnu tacku duži: ")
    x4 = input("Unesite x koordinatu za krajnu tacku duži: ")
    y4 = input("Unesite y koordinatu za krajnu tacku duži: ")

    duz2 = Duz(x3, y3, x4, y4)

    print "\nPrva duž ima pocetne koordinate (", duz1.x1, ",", duz1.y1, ") i krajne koordinate (",\
        duz1.x2, ",", duz1.y2, "), a njena duzina je", duz1.duzina()
    print "Druga duž ima pocetne koordinate (", duz2.x1, ",", duz2.y1, ") i krajne koordinate (",\
        duz2.x2, ",", duz2.y2, "), a njena duzina je", duz2.duzina()

    x_pom = input("\nUnesite dx pomeraj za krajnu tacku: ")
    y_pom = input("Unesite dy pomeraj za krajnu tacku: ")

    tacka2 = tacka2.pomeranje(x_pom, y_pom)
    duz1 = Duz.duz(tacka1, tacka2)

    print "\nNova duž ima pocetne koordinate (", duz1.x1, ",", duz1.y1, ") i krajne koordinate (",\
        duz1.x2, ",", duz1.y2, "), a njena duzina je", duz1.duzina()


if __name__ == '__main__':
    main()