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

    cursor = conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
    try:
        cursor.execute("""SELECT * from nacinkoriscenja""")
    except:
        print "Neuspesna selekcija iz nacinkoriscenja"

    rows = cursor.fetchall()
    print "\nRows: \n"
    row_count = 0
    for row in rows:
        row_count += 1
        print row_count, "   ", row[0], "|", row[1]


if __name__ == "__main__":
    main()