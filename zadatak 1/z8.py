# -*- coding: utf-8 -*-

x = int(input("Unesite petocifreni broj: "))

max = -1

for c in str(x):
    i = int(c)
    if i > max:
        max = i

print "\n Najveću cifru u broju je: ", max,
