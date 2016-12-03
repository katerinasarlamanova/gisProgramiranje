# -*- coding: utf-8 -*-

from inzenjer import *

def main():
    # Kreiranje objekata
    I = Inzenjer("Katerina", "Sarlamanova", "0210993465016", "25")
    G = GeodetskiInzenjer("Sanja", "Karova", "2303993465012", None , 2)
    E = ElektroInzenjer("Vera", "Petrova", "1710996465006", "65", 3)

    print I.ime, I.prezime
    print (I.info())
    print (G.info2())
    print (G.imaLicencu())
    G.licenca = 999
    print (G.imaLicencu())
    print (E.ime)
    print (E.licenca)
    print (E.info2())


if __name__ == '__main__':
    main()