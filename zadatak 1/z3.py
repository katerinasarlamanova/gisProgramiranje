# -*- coding: utf-8 -*-

def rezultat(aD, bD):
    razD = aD - bD
    razMinuti = ((razD - int(razD)) * 60)
    razSekunde = ((razMinuti - int(razMinuti)) * 60)
    rez = []
    rez.append(int(razD))
    rez.append(int(razMinuti))
    rez.append(int(round(razSekunde,0)))
    return rez

def uglovi():
    a = raw_input('Unesite prvi ugao u formatu xx:xx:xx : ')
    (stepeni, minute, secunde) = map(float, a.split(':'))

    b = raw_input('Unesite drugi ugao u formatu xx:xx:xx : ')
    (stepeni2, minute2, secunde2) = map(float, b.split(':'))

    aD = stepeni + minute / 60 + secunde / 3600 #ugao u decimale
    bD = stepeni2 + minute2 / 60 + secunde2 / 3600 #ugao u decimale

    (stepeni3, minute3, secunde3) = rezultat(aD,bD)

    print '\nRazlika dva uglova',int(stepeni),'°', int(minute),"'", int(secunde),'"', " i ", int(stepeni2),'°', int(minute2),"'", int(secunde2),'"',\
        'je:', int(stepeni3),'°', int(minute3),"'", int(secunde3),'"'

uglovi()