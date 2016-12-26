# -*- coding: utf-8 -*-
#!/usr/bin/env python

import psycopg2
import psycopg2.extras

class DetalnjaTacka:

    STABILIZACIJA = {1:"nestabilisana na terenu", 2:"stabilisana kamenom belegom"}

    def __init__(self, id, oznaka, stabil, koor):
        if stabil not in self.STABILIZACIJA:
            raise ValueError("%s Stabilizacija nije validnog tipa" % stabil)
        self._id = id
        self._oznaka = oznaka
        self._stabil = stabil
        self._koor = koor
        self._wkt = "point"

    def __str__(self):
        return "ID: %s\nOznaka: %s\nStabilizacija: %s\nKoordinate:%s" %(self.id, self.oznaka, self.stabil, self.koor)

    def __getitem__(self, item):
        return item

    @property
    def id(self):
        return self._id

    @property
    def oznaka(self):
        return self._oznaka

    @property
    def stabil(self):
        return self._stabil

    @property
    def koor(self):
        return self._koor

    @property
    def wkt(self):
        return self._wkt

    @id.setter
    def id(self, id):
        self._id = id

    @oznaka.setter
    def oznaka(self, oznaka):
        self._oznaka = oznaka

    @stabil.setter
    def stabil(self, stabil):
        self._stabil = stabil

    @koor.setter
    def koor(self, koor):
        self._koor = koor

    @wkt.setter
    def wkt(self, wkt):
        self._wkt = wkt

def main():

    p = DetalnjaTacka(10, "t2", 2, (8, 8))
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