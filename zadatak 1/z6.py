# -*- coding: utf-8 -*-

brojevi = []
broj1 = int(raw_input("Unesite prvi broj: "))
broj2 = int(raw_input("Unesite drugi broj: "))

brojevi.append(broj1)
brojevi.append(broj2)

max = max(brojevi)
min = min(brojevi)

print "\n Maksimum je: ", max, "\n"
print " Minimum je: ", min,