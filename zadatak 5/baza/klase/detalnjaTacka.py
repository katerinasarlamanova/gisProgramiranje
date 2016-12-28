# -*- coding: utf-8 -*-
#!/usr/bin/env python


class DetalnjaTacka:

    STABILIZACIJA = {1:"nestabilisana na terenu", 2:"stabilisana kamenom belegom"}

    def __init__(self, id, oznaka, stabil, koor):
        if stabil not in self.STABILIZACIJA:
            raise ValueError("%s Stabilizacija nije validnog tipa" % stabil)
        self._id = id
        self._oznaka = oznaka
        self._stabil = stabil
        self._koor = koor
        self._wkt = "point"

    def __str__(self):
        return "ID: %s\nOznaka: %s\nStabilizacija: %s\nKoordinate:%s" %(self.id, self.oznaka, self.stabil, self.koor)

    def __getitem__(self, item):
        return item

    @property
    def id(self):
        return self._id

    @property
    def oznaka(self):
        return self._oznaka

    @property
    def stabil(self):
        return self._stabil

    @property
    def koor(self):
        return self._koor

    @property
    def wkt(self):
        return self._wkt

    @id.setter
    def id(self, id):
        self._id = id

    @oznaka.setter
    def oznaka(self, oznaka):
        self._oznaka = oznaka

    @stabil.setter
    def stabil(self, stabil):
        self._stabil = stabil

    @koor.setter
    def koor(self, koor):
        self._koor = koor

    @wkt.setter
    def wkt(self, wkt):
        self._wkt = wkt

