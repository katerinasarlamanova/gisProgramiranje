# -*- coding: utf-8 -*-

#1
def zdravo():
    print("Zdravo, geoinformatičari!")


#2
def operacije():
    x = float(input("Unesite prvi broj: "))
    y = float(input("Unesite drugi broj: "))
    #brojeve su uzeti kao float da bi moglo da se izračuna ostatak pri delenja

    d = (x/y)

    print "\nUneta vrednost za x je: " , int(x)
    print "Uneta vrednost za y je: " , int(y)
    print int(x) , " + " , int(y) , " = " , int(x + y)
    print int(x) , " - " , int(y) , " = " , int(x - y)
    print int(x) , " * " , int(y) , " = " , int(x * y)
    print int(x) , " / " , int(y) , " = " , ("%.2f" %d)
    print "Ceo broj delenja x sa y je: " , int(x // y)
    print "Ostatak delenja x sa y je: " , int(x % y)


#3
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


#4
def dva4broja():
    broj1 = int(input("Unesite prvi četvorocifreni broj: "))
    broj2 = int(input("Unesite drugi četvorocifreni broj: "))
    rez = s(broj1,broj2)
    print rez

def s(broj1,broj2):
    zbir = 0

    while (broj2 > 0):
        n = broj2 % 10
        zbir = zbir + n
        broj2 = broj2 // 10

    print("\nSuma cifara drugog četvorocifrenog broja je : %d" % zbir)

    cifre = []

    while broj1> 0:
        cifre.append(broj1%10)
        broj1 //= 10

    s = 0
    p = 0
    i = 0
    for cifra in reversed(cifre):
        if i%2 == 0:
            s += cifra
        else:
            p += cifra
        i += 1

    print '\nRazlika između sume na parne i neparne pozicije prvog četvorocifrenog broja je: ', s-p
    return""


#5
def sredina():
    a = int(raw_input("Unesite prvi broj: "))
    b = int(raw_input("Unesite drugi broj: "))
    c = int(raw_input("Unesite treci broj: "))

    s = (a + b + c) / 3.0

    print ("Sredina unetih brojeva je %.3f" %s)
    # %.3f zaokruzava na 3 decimale


#6
def rez(broj1,broj2):
    if broj1 == broj2:
        print "\nBrojevi su jednaki"
    elif broj1 > broj2:
        max = broj1
        min = broj2
        print "\nMaksimum je: ", max
        print "Minimum je: ", min
    elif broj1 < broj2:
        max = broj2
        min = broj1
        print "\nMaksimum je: ", max
        print "Minimum je: ", min
    return ""

def minMax():
    broj1 = int(raw_input("Unesite prvi broj: "))
    broj2 = int(raw_input("Unesite drugi broj: "))

    m = rez(broj1,broj2)
    print m

#7
def zbirPozBr():
    broj1 = int(raw_input("Unesite prvi broj: "))
    broj2 = int(raw_input("Unesite drugi broj: "))
    broj3 = int(raw_input("Unesite treci broj: "))
    broj4 = int(raw_input("Unesite cetvrti broj: "))

    rez = brojevi(broj1,broj2,broj3,broj4)
    print rez

def brojevi(broj1,broj2,broj3,broj4):
    brojevi = []
    if (broj1 > 0):
        brojevi.append(broj1)

    if (broj2 > 0):
        brojevi.append(broj2)

    if (broj3 > 0):
        brojevi.append(broj3)

    if (broj4 > 0):
        brojevi.append(broj4)

    zbir = (sum(brojevi))

    print "\nZbir pozitivnih brojeva je: ", zbir
    return""

#8
def najvecaCifra():
    x = int(input("Unesite petocifreni broj: "))

    max = -1

    for c in str(x):
        i = int(c)
        if i > max:
            max = i

    print "\n Najveću cifru u broju je: ", max

#9
def rez(x):
    x_ascii = ord(x)
    if x.isdigit():
        print '\nUneti karakter je: ' ,x , '\nNjegov ASCII kod je: ',x_ascii
    else:
        print '\nUneti karakter je: ' ,x , '\nNjegov ASCII kod je: ',x_ascii
        print 'Odgovarajuče veliko slovo je: ', x.upper(), '\nOdgovarajuče malo slovo je: ' ,x.lower()
    return ""

def kod():
    x = unicode(raw_input('Unesite neki karakter: '))
    rezultat = rez(x)
    print rezultat

#10
def brojCifre():
    x = unicode(raw_input('Unesite pet karaktera: '))
    cifre = sum(c.isdigit() for c in x)

    print '\nBroj cifara je: ' ,cifre

#11
import math

def rastojanje(a1, b1, a2, b2):
    duzina = math.sqrt((a1 - a2)**2 + (b1 - b2)**2)
    return duzina

def tacka():
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

#12
import sys

def min(novcanice, x):
  # Najmanji broj novčanica koje je potrebno izdvojiti prilikom plaćanja proizvoda
  # Ako ne postoji novcanica za sumu vraća 0
  rez = None

  if x == 0:
    rez = { }
    for nov in novcanice:
      rez[nov] = 0
  elif len(novcanice) == 0:
    # Ako suma je nula onda i rezultat je nula
    # Ako suma nije nula, ali ne postoji novčanica za ta suma, rezultat je nula

     rez = None
  else:
    # Suma nije nula i postoje novcaniče za tu sumu
    nov = novcanice[0]
    ostatak = novcanice[1:]

    max_broj = x / nov
    min_broj_novcanice = sys.maxint

    # moguće kombinacije
    for i in range(max_broj + 1):
      trenutrna_vrednost = x - (nov * i)
      ostatak_rez = min(ostatak, trenutrna_vrednost)

      if ostatak_rez != None:
        nova_vrednost = i + sum(ostatak_rez.values())

        if nova_vrednost < min_broj_novcanice:
          min_broj_novcanice = nova_vrednost
          rez = ostatak_rez
          rez[nov] = i

  return rez


def printaj_rezultat(novcanice, x, rez):
  print "Najmanji broj novčanice za ", x, "koristeći novčanice:", novcanice, "je: "
  if rez == None:
    print "  Ne postoji takva novčanica"
  else:
    print "  %d novčanice" % sum(rez.values())
    print "  date redosledom: ", sorted(rez.items())
  print


def minNovcanice():
  x = int(input('Unesite sumu: '))
  novcanice = [5000, 2000, 1000, 200, 100, 50, 20, 10, 1]
  rez = min(novcanice, x)
  printaj_rezultat(novcanice, x, rez)

#13
def kUn():
    n = int(input("Unesite prvi broj: "))
    k = int(input("Unesite drugi broj: "))

    p = n
    i = 0
    while ((p // k) !=0) :
        p = p - k
        i = i + 1

    print "\nBroj",k, "se u broj",n, "pojavljuje" ,i, "puta"

#14
def sumaRazlika():
    x = int(input('Unesite broj: '))
    rez = cifre(x)
    print rez

def cifre(x):
    cifre = []

    while x > 0:
        cifre.append(x%10)
        x //= 10

    s = 0
    p = 0
    i = 0
    for cifra in reversed(cifre):
        if i%2 == 0:
            s += cifra
        else:
            p += cifra
        i += 1

    print 'Suma brojeva na parnim mestima je: ', s
    print 'Suma brojeva na neparnim mestima je: ', p
    print 'Razlika između sume je: ', s-p
    return ""