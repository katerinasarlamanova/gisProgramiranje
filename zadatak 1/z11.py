# -*- coding: utf-8 -*-

import math

def rastojanje(a1, b1, a2, b2):
    duzina = math.sqrt((a1 - a2)**2 + (b1 - b2)**2)
    return duzina

x1 = float(input('Unesite x1 koordinata: '))
y1 = float(input('Unesite y1 koordinata: '))
x2 = float(input('Unesite x2 koordinata: '))
y2 = float(input('Unesite y2 koordinata: '))
x3 = float(input('Unesite x3 koordinata: '))
y3 = float(input('Unesite y3 koordinata: '))

x = float(input('Unesite x koordinata za tacku: '))
y = float(input('Unesite y koordinata za tacku: '))

strana1 = rastojanje(x1, y1, x2, y2)    #rastojanje od jedna do druga tacka iz torugao
strana2 = rastojanje(x2, y2, x3, y3)
strana3 = rastojanje(x1, y1, x3, y3)

str4 = rastojanje(x, y, x1, y1)    #rastojanje od tacka P do neka tacka iz torugao
str5 = rastojanje(x, y, x2, y2)
str6 = rastojanje(x, y, x3, y3)

p = (strana1 + strana2 + strana3) / 2

p1 = (strana1 + str4 + str5) / 2
p2 = (strana2 + str5 + str6) / 2
p3 = (strana3 + str4 + str6) / 2

povrs = math.sqrt(p * (p - strana1) * (p - strana2) * (p - strana3))    #ukupna površ trougao

povrs1 = math.sqrt(p1 * (p1 - strana1) * (p1 - str4) * (p1 - str5))    #površ trouglove formirani sa tačkom P
povrs2 = math.sqrt(p2 * (p2 - strana2) * (p2 - str5) * (p2 - str6))
povrs3 = math.sqrt(p3 * (p3 - strana3) * (p3 - str4) * (p3 - str6))

if povrs == (povrs1 + povrs2 + povrs3):
    print "\n DA"
else:
    print "\n NE"
