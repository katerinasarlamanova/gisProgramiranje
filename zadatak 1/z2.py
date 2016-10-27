# -*- coding: utf-8 -*-

x = float(input("Unesite prvi broj: "))
y = float(input("Unesite drugi broj: "))
#brojeve su uzeti kao float da bi moglo da se izračuna ostatak pri delenja

d = (x/y)

print("Uneta vrednost za x je: ") + str(x)
print("Uneta vrednost za y je: ") + str(y)
print str(x) + (" + ") + str(y) + (" = ") + str(x + y)
print str(x) + (" - ") + str(y) + (" = ") + str(x - y)
print str(x) + (" * ") + str(y) + (" = ") + str(x * y)
print str(x) + (" / ") + str(y) + (" = ") + ("%.2f" %d)
print("Ceo broj delenja x sa y je: ") + str(x // y)
print("Ostatak delenja x sa y je: ") + str(x % y)