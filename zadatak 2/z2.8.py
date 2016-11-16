# -*- coding: utf-8 -*-

def proizvodElemenata(lista):
    proizvod = 1
    for i in lista:
        proizvod = proizvod * i
    return proizvod

def main():
    inp = raw_input('Unesite niz brojeva razdeljeni zapirkom: ')
    lista = map(int, inp.split(','))
    print lista

    proizvod = proizvodElemenata(lista)

    print "Proizvod brjeva u nizi je:",proizvod

main()