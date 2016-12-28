#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import sys
import psycopg2
from baza.klase.poligon import *
from baza.klase.detalnjaTacka import *
from GUIp import *
from ast import literal_eval


class ExampleApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.konekcija)
        self.pushButton_2.clicked.connect(self.tacke)
        self.pushButton_3.clicked.connect(self.parcele)
        self.pushButton_4.clicked.connect(self.p)
        self.pushButton_5.clicked.connect(self.t)


    def konekcija(self):
        try:
            conn = psycopg2.connect(dbname='python', user='postgres', host='localhost', password='teodora2001')
            print "Uspesna konekcija", conn
        except:
            print "Neuspesna konekcija"


    def tacke(self):
        conn_string = "dbname='python' user='postgres' host='localhost' password='teodora2001'"

        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT * from tacka""")
        except:
            print "Neuspesna selekcija iz tacka"

        rows = cursor.fetchall()
        for row in rows:
            d = DetalnjaTacka(row[0], row[1], row[2], row[3])
            print "\n", d


    def parcele(self):
        conn_string = "dbname='python' user='postgres' host='localhost' password='teodora2001'"

        conn = psycopg2.connect(conn_string)
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

        for row in rows:
            p = Parcela("id.poligona", row[0], row[1], row[2])

            for ra in rows3:

                for r in rows2:
                    par = r[1]

                    if int(row[0]) == int(par) and int(r[2]) == int(ra[0]):
                        d = DetalnjaTacka(ra[0], ra[1], ra[2], literal_eval(ra[3]))
                        p.dodajTacka(d)

            print "\n", p


    def p(self):
        x = str(self.textEdit.toPlainText())

        conn_string = "dbname='python' user='postgres' host='localhost' password='teodora2001'"

        conn = psycopg2.connect(conn_string)
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

        for row in rows:
            if x == row[1]:
                p = Parcela("id.poligona", row[0], x, row[2])
                for ra in rows3:
                    for r in rows2:
                        par = r[1]
                        if int(row[0]) == int(par) and int(r[2]) == int(ra[0]):
                            d = DetalnjaTacka(ra[0], ra[1], ra[2], literal_eval(ra[3]))
                            p.dodajTacka(d)
                print p, "\n"

                self.label_11.setText(str(p.areaPoligona()))
                self.label_12.setText(str(p.br()))
                self.label_13.setText(str(p.nacin))
                self.label_14.setText(str(p.wkt))


    def t(self):
        y = str(self.textEdit_6.toPlainText())

        conn_string = "dbname='python' user='postgres' host='localhost' password='teodora2001'"

        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        try:
            cursor.execute("""SELECT * from tacka""")
            cursor2.execute("""SELECT * FROM tackeparcela""")
        except:
            print "Neuspesna selekcija iz tacka"

        rows = cursor.fetchall()
        rows2 = cursor2.fetchall()
        for row in rows:
            if y == str(row[0]):
                t = DetalnjaTacka(y, row[1], row[2], row[3])
                print t, "\n"

                x = t.koor.split(",")[0]
                y = t.koor.split(",")[1]
                xx = x.split("(")[1]
                yy = y.split(")")[0]

                self.label_18.setText(str(xx))
                self.label_15.setText(str(yy))
                self.label_17.setText(str(t.wkt))
                #self.label_16.setText(str(t.wkt))

                list = []
                for r in rows2:
                    list.append(int(r[2]))

                if int(t.id) in list:
                    self.label_16.setText("DA")
                else:
                    self.label_16.setText("NE")


def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
