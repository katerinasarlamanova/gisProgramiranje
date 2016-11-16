# -*- coding: utf-8 -*-

# Proizvod dve matrice koristeči list comprehensions

def main():
    a1 = int(input("Unesite a1.1 za prvu matricu: "))
    b1 = int(input("Unesite a1.2 za prvu matricu: "))
    c1 = int(input("Unesite a1.3 za prvu matricu: "))
    a2 = int(input("Unesite a2.1 za prvu matricu: "))
    b2 = int(input("Unesite a2.2 za prvu matricu: "))
    c2 = int(input("Unesite a2.3 za prvu matricu: "))
    a3 = int(input("Unesite a3.1 za prvu matricu: "))
    b3 = int(input("Unesite a3.2 za prvu matricu: "))
    c3 = int(input("Unesite a3.3 za prvu matricu: "))
    d1 = int(input("Unesite a1.1 za drugu matricu: "))
    e1 = int(input("Unesite a1.2 za drugu matricu: "))
    f1 = int(input("Unesite a1.3 za drugu matricu: "))
    d2 = int(input("Unesite a2.1 za drugu matricu: "))
    e2 = int(input("Unesite a2.2 za drugu matricu: "))
    f2 = int(input("Unesite a2.3 za drugu matricu: "))
    d3 = int(input("Unesite a3.1 za drugu matricu: "))
    e3 = int(input("Unesite a3.2 za drugu matricu: "))
    f3 = int(input("Unesite a3.3 za drugu matricu: "))

    X = [[a1,b1,c1],
        [a2,b2,c2],
        [a3,b3,c3]]

    Y = [[d1,e1,f1],
        [d2,e2,f2],
        [d3,e3,f3]]

    rez = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

    for r in rez:
        print (r)

main()