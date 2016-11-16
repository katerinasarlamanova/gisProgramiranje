# -*- coding: utf-8 -*-

import math

print("Algoritam za rješavanje kvadratne jednadžbe ax^2 + bx + c = 0")

def main():
    x1 = 0
    x2 = 0
    a = float(input("Unesite a: "))
    b = float(input("Unesite b: "))
    c = float(input("Unesite c: "))

    # računanje diskriminante
    d = b ** 2 - 4 * a * c

    # provjera uvjeta
    if d < 0:
        # ovde koristimo round() funkciju za određivanje broja decimalnih mesta
        print "\nJednačina nema realnih rešenja zato što je D < 0:", round(d, 4)
    elif d == 0:
        x1 = (-b) / (2 * a)
        print "\nJednačina ima jedno dvostruko rešenje  zato što je D = 0: ", round(x1, 4)
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print "\nJednačina ima dva rešenja  zato što je D > 0:", round(d, 4)
        print "Rešenje x1:", round(x1, 4)
        print "Rešenje x2:", round(x2, 4)

main()