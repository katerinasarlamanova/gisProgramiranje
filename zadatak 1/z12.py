# -*- coding: utf-8 -*-

import sys

x = int(input('Unesite sumu: '))
novcanice = [5000, 2000, 1000, 200, 100, 50, 20, 10, 1]

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

rez = min(novcanice, x)
printaj_rezultat(novcanice, x, rez)