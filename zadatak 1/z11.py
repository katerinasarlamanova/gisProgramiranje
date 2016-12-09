# -*- coding: utf-8 -*-

import math

import math

def rastojanje(a1, b1, a2, b2):
    duzina = math.sqrt((a1 - a2)**2 + (b1 - b2)**2)
    return duzina

xa = int(input('Unesite x koordinata za teme A: '))
ya = int(input('Unesite y koordinata za teme A: '))
xb = int(input('Unesite x koordinata za teme B: '))
yb = int(input('Unesite y koordinata za teme B: '))
xc = int(input('Unesite x koordinata za teme C: '))
yc = int(input('Unesite y koordinata za teme C: '))

x = int(input('Unesite x koordinata za tacku: '))
y = int(input('Unesite y koordinata za tacku: '))

AB = rastojanje(xa, ya, xb, yb)    #rastojanje od jedna do druga tacka iz torugao
BC = rastojanje(xb, yb, xc, yc)
AC = rastojanje(xa, ya, xc, yc)

EA = rastojanje(x, y, xa, ya)      #rastojanje od tacka E do neka tacka iz torugao
EB = rastojanje(x, y, xb, yb)
EC = rastojanje(x, y, xc, yc)

AEB = math.acos((EA * EA + EB * EB - AB * AB) / (2 * EA * EB))
BEC = math.acos((EB * EB + EC * EC - BC * BC) / (2 * EB * EC))
CEA = math.acos((EA * EA + EC * EC - AC * AC) / (2 * EA * EC))

ugao = math.degrees(AEB) + math.degrees(BEC) + math.degrees(CEA)

print round(ugao, 1)

if (round(ugao, 1) == 360.0):
    print "\nDA"
else:
    print "\nNE"