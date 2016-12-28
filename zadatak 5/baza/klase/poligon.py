# -*- coding: utf-8 -*-
#!/usr/bin/env python

from detalnjaTacka import *
import numpy as np


class Poligon:

    tacka = DetalnjaTacka(None, "", 2, None)

    def __init__(self, id):
        self._id = id
        self._wkt = "polygon"
        self.povrs = []

    def dodajTacka(self, tacka):
        self.tacka = tacka
        self.povrs.append(self.tacka)

    def __str__(self):
        return "ID_poligon: %s \nBr tacaka: %s \nKoolekcija tacaka: %s \nPovršina: %s" %(self.id, self.br(), self.povrs, self.areaPoligona())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def wkt(self):
        return self._wkt

    @wkt.setter
    def wkt(self, wkt):
        self._wkt = wkt

    def br(self):
        return len(self.povrs)

    def areaPoligona(self):
        m = len(self.povrs)
        self.area = 0.0
        self.koordinate = []
        for i in range(m):
            k = self.povrs[i].koor
            self.koordinate.append(k)
        n = len(self.koordinate)
        for i in range(n):
            j = (i + 1) % n
            self.area += self.koordinate[i][0] * self.koordinate[j][1]
            self.area -= self.koordinate[j][0] * self.koordinate[i][1]
        self.area = abs(self.area) / 2.0
        return self.area


class Parcela(Poligon):

    def __init__(self, id, idp, oznaka, nacin):
        Poligon.__init__(self, id)
        self._idp = idp
        self._oznaka = oznaka
        self._nacin = nacin

    def __str__(self):
        return Poligon.__str__(self) + ("\nID_parcela: %s \nOznaka: %s \nNacin koriscenja: %s" %(self.idp, self.oznaka, self.nacin))

    @property
    def idp(self):
        return self._idp

    @idp.setter
    def idp(self, idp):
        self._idp = idp

    @property
    def oznaka(self):
        return self._oznaka

    @oznaka.setter
    def oznaka(self, oznaka):
        self._oznaka = oznaka

    @property
    def nacin(self):
        return self._nacin

    @nacin.setter
    def nacin(self, nacin):
        self._nacin = nacin

