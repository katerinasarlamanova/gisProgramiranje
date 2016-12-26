# -*- coding: utf-8 -*-
#!/usr/bin/env python

import psycopg2

try:
    conn = psycopg2.connect(dbname='python', user='postgres', host='localhost', password='teodora2001')
except:
    print "Neuspesna konekcija"


