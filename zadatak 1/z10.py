# -*- coding: utf-8 -*-

x = unicode(raw_input('Unesite pet karaktera: '))

cifre = sum(c.isdigit() for c in x)

print '\n Broj cifara je: ' ,cifre