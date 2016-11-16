# -*- coding: utf-8 -*-

def sumaElemenata(lista):
    zbir = 0
    for i in lista:
        zbir = zbir + i
    return zbir

def main():
    inp = raw_input('Unesite niz brojeva razdeljeni zapirkom: ')
    lista = map(int, inp.split(','))
    print lista

    suma = sumaElemenata(lista)

    print "Suma brjeva u nizi je:",suma

main()