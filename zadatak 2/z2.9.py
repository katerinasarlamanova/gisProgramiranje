# -*- coding: utf-8 -*-

def main():
    lista1 = raw_input("Unesite elementi prvog niza odvojene zarezima: ")
    lista2 = raw_input("Unesite elementi prvog niza odvojene zarezima: ")
    n1 = lista1.split(",")
    n2 = lista2.split(",")
    op = raw_input("p - prvo ide elemet prvog niza, d - prvo ide element drugog niza ")
    if op == 'p':
        o = True
    else:
        o = False
    print (naizmenicno(n1, n2, o))

def naizmenicno(lista1, lista2, o):
    i = 0
    r = list()
    if len(lista1) > len(lista2):
        d = len(lista1)
    else:
        d = len(lista2)
    while i < d:
        if o:
            r.append(int(lista1[i]))
            r.append(int(lista2[i]))
        else:
            r.append(int(lista2[i]))
            r.append(int(lista1[i]))
        i+=1
    return r

main()