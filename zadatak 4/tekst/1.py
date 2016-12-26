# -*- coding: utf-8 -*-
#!/usr/bin/env python

reset = "\033[0;0m"
red = '\033[91m'

a = raw_input("Za pisanje u datoteci izaberite" + red + " p" + reset + ", za čitanje iz datoteci izaberite" + red + " c" + reset + ": ")
if (a == "c"):
    f = open('Ulazni_Podaci.txt', 'r')
    b = raw_input("Izaberite način citanja, za citanja ceo dokument izaberite" + red + " sve" + reset +
                  ", za ispisavanje liniju po liniju sa rednim brojom izaberite" + red + " linija" + reset + ": ")
    if (b == "sve"):
        print f.read()
    elif (b == "linija"):
        for i, line in enumerate(f, start = 1):
            print i, line

    f.close()
elif (a == "p"):
    b = raw_input("Izaberite način pisanja, za odavanjem unetog sadržaja na kraj postojećeg sadržaja datoteke izaberite" + red +
                  " dodaj" + reset + ", za obrisati postojeći sadržaj datoteke izaberite" + red + " obrisi" + reset + ": ")
    if (b == "dodaj"):
        f = open('Ulazni_Podaci.txt', 'a')
        n = raw_input("Unos: ")
        f.write(n)

        f.close()
    elif (b == "obrisi"):
        f = open('Ulazni_Podaci.txt', 'w')
        n = raw_input("Unos: ")
        f.write(n)

        f.close()