# -*- coding: utf-8 -*-

def sums(lista):
    total = 0
    for i in lista:
        if i % 2 == 0:
            total += i
    return total

def main():
    inp = raw_input('Unesite niz brojeva razdeljeni zapirkom: ')
    lista = map(int, inp.split(','))
    print lista
    s = sums(lista)
    print 'Suma parnih elemenata u nizi je: ', s

main()