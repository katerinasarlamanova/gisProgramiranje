# -*- coding: utf-8 -*-
#!/usr/bin/env python

import psycopg2
import psycopg2.extras
from baza.klase.detalnjaTacka import *


def main():

    a = int(input("ID tačka: "))
    b = raw_input("Oznaka tačka: ")
    c = int(input("Stabilizacija tačka (može da bude 1 ili 2): "))
    d = input("Koordinate tačka format(x,y): ")

    p = DetalnjaTacka(a, b, c, d)
    print "\n", p, "\n"

    conn_string = "dbname='python' user='postgres' host='localhost' password='teodora2001'"
    print "Connecting to database\n	->%s" % (conn_string)

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    query = ("""INSERT INTO tacka (id_tacka, oznaka, nacinstabilizacija, koordinate) VALUES (%s, %s, %s, %s);""")
    data = (str(p.id), str(p.oznaka), str(p.stabil), str(p.koor))
    try:
        cursor.execute(query, data)
        conn.commit()

    except:            #(Exception, psycopg2.DatabaseError) as error: print(error)
        print "\nNeuspesno ubacivanje podataka u tabelu tacka"

if __name__ == "__main__":
     main()