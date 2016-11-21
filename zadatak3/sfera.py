# -*- coding: utf-8 -*-

class Sfera:
    broj = 0  # Klasna promenljiva koja broji objekte klase
    poluprecnik = 0  #Instancne promenljive: poluprecnik i koordinate centra (xCentar, yCentari, zCentar)
    xCentar = 0
    yCentar = 0
    zCentar = 0

    def __init__(self):           # Konstruktor jedinične sfere u koordinatni pocetak 0
        self.poluprecnik = 1.00   # Ostale instancne promenljive bice postavljene podrazumevano na 0
        Sfera.broj += 1           # Uvecava se broj kreiranih objekata

    def __init__(self, x, y, z):  # Konstruktor jedinične sfere u zadatom tackom
        self.poluprecnik = 1.00
        self.xCentar = x
        self.yCentar = y
        self.zCentar = z
        Sfera.broj += 1           # Uvecava se broj kreiranih objekata

    def __init__(self, r, x, y, z):   # Konstruktor sfere sa zadatim parametrima
        self.poluprecnik = r
        self.xCentar = x
        self.yCentar = y
        self.zCentar = z
        Sfera.broj += 1           # Uvecava se broj kreiranih objekata

    def zapremina(self):          # Metod koj računa zapremina
        r = self.poluprecnik
        self.volume = 1.3333333333 * 3.14 * (r * r * r)
        return (self.volume)

    @staticmethod
    def brojKreiranihObjekata():
        return Sfera.broj
