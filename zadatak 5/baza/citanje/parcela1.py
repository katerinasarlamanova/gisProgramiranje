# -*- coding: utf-8 -*-
#!/usr/bin/env python

import psycopg2
import psycopg2.extras

def main():
    conn_string = "dbname='python' user='postgres' host='localhost' password='teodora2001'"
    print "Connecting to database\n	->%s" % (conn_string)

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    work_mem = 2048

    cursor.execute('SET work_mem TO %s', (work_mem,))

    cursor.execute('SHOW work_mem')

    memory = cursor.fetchone()

    print "Value: ", memory[0]
    print "Row:	", memory
    print "\n"

    cursor = conn.cursor()
    cursor2 = conn.cursor()
    cursor3 = conn.cursor()

    try:
        cursor.execute("""SELECT * from parcela""")
        cursor2.execute("""SELECT * FROM tackeparcela""")
        cursor3.execute("""SELECT * FROM tacka""")

    except:
        print "Neuspesna selekcija iz parcela"

    rows = cursor.fetchall()
    rows2 = cursor2.fetchall()
    rows3 = cursor3.fetchall()
    print "\nRows  ID  Oznaka   Koršcenja   Kolekcija tačaka\n"
    row_count = 0

    for row in rows:
        tacke = []
        row_count += 1
        for ra in rows3:

            for r in rows2:
                par = r[1]

                if int(row[0]) == int(par) and int(r[2]) == int(ra[0]):
                    tacke.append(ra[3])

        print row_count, "   ", row[0], " | ", row[1], " | ", row[2], " | ", tacke


if __name__ == "__main__":
    main()