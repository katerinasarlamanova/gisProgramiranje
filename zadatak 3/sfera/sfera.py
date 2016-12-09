# -*- coding: utf-8 -*-

class Sfera:
    broj = 0  # Klasna promenljiva koja broji objekte klase

    @classmethod
    def jedinicna(cls):           # Konstruktor jedinične sfere u koordinatni pocetak 0
        cls.poluprecnik = 1.00   # Ostale instancne promenljive bice postavljene podrazumevano na 0
        jedinicna = Sfera(cls.poluprecnik, 0 , 0 , 0)
        return jedinicna

    @classmethod
    def sfxyz(cs, x, y, z):  # Konstruktor jedinične sfere u zadatom tackom
        cs.poluprecnik = 1.00
        cs.xCentar = x
        cs.yCentar = y
        cs.zCentar = z
        sf = Sfera(cs.poluprecnik, x, y, z)
        return sf

    def __init__(self, r, x, y, z):   # Konstruktor sfere sa zadatim parametrima
        self.poluprecnik = r
        self.xCentar = x
        self.yCentar = y
        self.zCentar = z
        Sfera.broj += 1           # Uvecava se broj kreiranih objekata

    def zapremina(self):          # Metod koj računa zapremina
        if (self.poluprecnik == 1):
            self.volume = 1.3333333333 * 3.14
            return (self.volume)
        else:
            r = self.poluprecnik
            self.volume = 1.3333333333 * 3.14 * (r * r * r)
            return (self.volume)

    @staticmethod
    def brojKreiranihObjekata():
        return Sfera.broj
