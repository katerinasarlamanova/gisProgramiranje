# -*- coding: utf-8 -*-

import operator

def proizvod(vektor1, vektor2):
    proizvod = reduce( operator.add, map( operator.mul, vektor1, vektor2))
    return proizvod

def main():
    a = int(input("Unesite pravac za vektor1: "))
    b = int(input("Unesite smer za vektor1: "))
    c = int(input("Unesite intenzitet za vektor1: "))
    d = int(input("Unesite pravac za vektor2: "))
    e = int(input("Unesite smer za vektor2: "))
    f = int(input("Unesite intenzitet za vektor2: "))

    vektor1 = (a, b, c)
    vektor2 = (d, e, f)

    s = proizvod(vektor1, vektor2)

    print "Skalarni proizvod za vektor1", vektor1, "i vektor2", vektor2, "je", s

main()
