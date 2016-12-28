# -*- coding: utf-8 -*-
#!/usr/bin/env python


import psycopg2
import psycopg2.extras
from baza.klase.poligon import *


def main():

    e = int(input("ID poligon: "))
    f = int(input("ID parcela: "))
    g = raw_input("Oznaka parcela format xxx/xx: ")
    h = int(input("Način koriščenja parcele: "))

    par = Parcela(e, f, g, h)

    br = int(input("\nUnesite broj tačaka u parceli: "))
    i = 0
    while (i < br):
        a = int(input("\nID tačka: "))
        b = raw_input("Oznaka tačka: ")
        c = int(input("Stabilizacija tačka (može da bude 1 ili 2): "))
        d = input("Koordinate tačka format(x,y): ")
        i = i + 1

        p = DetalnjaTacka(a, b, c, d)
        print "\n", p

        par.dodajTacka(p)

    print "\n", par

    conn_string = "dbname='python' user='postgres' host='localhost' password='teodora2001'"
    print "\nConnecting to database\n	->%s" % (conn_string)

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    query = ("""INSERT INTO parcela (id_parcela, brojparcele, nacinkoriscenja) VALUES (%s, %s, %s);""")
    data = (str(par.idp), str(par.oznaka), str(par.nacin))

    try:
        cursor.execute(query, data)
        conn.commit()

    except:
         print "\nNeuspesno ubacivanje podataka u tabelu parcela"

    m = len(par.povrs)
    for i in range(m):
        query2 = ("""INSERT INTO tacka (id_tacka, oznaka, nacinstabilizacija, koordinate) VALUES (%s, %s, %s, %s);""")
        data2 = (str(par.povrs[i].id), str(par.povrs[i].oznaka), str(par.povrs[i].stabil), str(par.povrs[i].koor))

        join = ("""INSERT INTO tackeparcela (id_parcela, id_tacka) VALUES (%s, %s);""")
        ids = (str(par.idp), str(par.povrs[i].id))

        try:
            cursor.execute(query2, data2)
            cursor.execute(join, ids)
            conn.commit()

        except: #(Exception, psycopg2.DatabaseError) as error: print(error)
            print "\nNeuspesno ubacivanje podataka u tabelu tacka"
            print "\nNeuspesno ubacivanje podataka u tabelu tackeparcela"

if __name__ == "__main__":
    main()