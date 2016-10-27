# -*- coding: utf-8 -*-

n = int(input("Unesite prvi broj: "))
k = int(input("Unesite drugi broj: "))

p = n
i = 0
while ((p // k) !=0) :
    p = p - k
    i = i + 1


print "\n Broj ",k, " se u broj ",n, " pojavljuje " ,i, " puta"