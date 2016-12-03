# -*- coding: utf-8 -*-

import random
import math
import itertools

def poligon():
    operator = raw_input("Unesite ime, prezime operatora i e-mail: ")
    c = int(input("Unesite broj tacaka koje formiraju poligon (najmanje tri): "))
    i = 0
    povrs = []          # Skup (pseudo)slučajnih tačaka
    while (i < c):      # Generisanje random tacke
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        z = random.randint(0, 100)
        tacka = (x, y, z)
        povrs.append(tacka)
        i = i + 1

    def areaPoligona(povrs):     # Funkcija koja računa površina poligona
        n = len(povrs)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += povrs[i][0] * povrs[j][1]
            area -= povrs[j][0] * povrs[i][1]
        area = abs(area) / 2.0
        return area

    def rastojanje(povrs):      # Funkcija koja računa rastojanje između dve najbliže tacke u poligonu
        p0, p1 = povrs
        return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

    def elevacija(parZ):        # Funkcija koja računa elevacija između dve tacke u poligonu (najniža i najviša)
        p0, p1 = parZ
        return (p0[2] - p1[2])

    area = areaPoligona(povrs)
    centroide = ((sum(d[0] for d in povrs)) / len(povrs), (sum(d[1] for d in povrs)) / len(povrs))
    maksimalnu = max(povrs, key=lambda item: item[0:1])
    minimalnu = min(povrs, key=lambda item: item[0:1])
    metadata  = [(ix, povrs[ix]) for ix in range(len(povrs))]

    minPar = min(itertools.combinations(povrs, 2), key=rastojanje)
    minRastojanje = rastojanje(minPar)

    parZ = max(itertools.combinations(povrs, 2), key=elevacija)
    zRastojanje = elevacija(parZ)

    print "\n", povrs
    print "Broj tacaka u poligonu je:", i
    print "\nPovršina poligona je:", area
    print "Sredina poligona je:", centroide
    print "\nMaksimalne vrednosti koordinata tačaka površi:", maksimalnu
    print "Minimalne vrednosti koordinata tačaka površi:", minimalnu
    print "\nTacke sa odgovarajuce indekse kao Id-ove:\n", metadata
    print "\nDve najbliže tacke su", minPar, "a rastojanje mešu njima je", minRastojanje
    print "Elevacija između dve tacke, najniža i najviša", parZ, "je", zRastojanje
    print "\nPovrš analizira operator: ", operator
    return ""
