# -*- coding: utf-8 -*-

brojevi = []
broj1 = int(raw_input("Unesite prvi broj: "))
broj2 = int(raw_input("Unesite drugi broj: "))
broj3 = int(raw_input("Unesite treci broj: "))
broj4 = int(raw_input("Unesite cetvrti broj: "))

if (broj1 > 0):
    brojevi.append(broj1)

if (broj2 > 0):
    brojevi.append(broj2)

if (broj3 > 0):
    brojevi.append(broj3)

if (broj4 > 0):
    brojevi.append(broj4)

zbir = (sum(brojevi))

print "\n Zbir pozitivnih brojeva je: ", zbir,