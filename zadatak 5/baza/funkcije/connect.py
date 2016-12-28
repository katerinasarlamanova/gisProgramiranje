# -*- coding: utf-8 -*-
#!/usr/bin/env python

import psycopg2

def konekcija():

    try:
        conn = psycopg2.connect(dbname='python', user='postgres', host='localhost', password='teodora2001')
        print "Uspesna konekcija", conn
    except:
        print "Neuspesna konekcija"

if __name__ == '__main__':
    konekcija()