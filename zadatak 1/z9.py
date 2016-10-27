# -*- coding: utf-8 -*-

x = unicode(raw_input('Unesite neki karakter: '))

x_ascii = ord(x)

if x.isdigit():
    print '\n Uneti karakter je: ' ,x , '\n Njegov ASCII kod je: ',x_ascii
else:
    print '\n Uneti karakter je: ' ,x , '\n Njegov ASCII kod je: ',x_ascii
    print ' Odgovarajuče veliko slovo je: ', x.upper(), '\n Odgovarajuče malo slovo je: ' ,x.lower()