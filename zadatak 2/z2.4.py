# -*- coding: utf-8 -*-

import math

def vektor(v):
    s = 0
    for k in v:
        s += float(k)**2
    return math.sqrt(s)

def intenzitet():
    u = raw_input("Unesite komponente vektora odvojene zarezima: ")
    v = u.split(",")
    print "Intenzitet vektora (", u, ") je", vektor(v)

intenzitet()