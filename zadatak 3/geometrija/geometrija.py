# -*- coding: utf-8 -*-

import math
import copy

class Tacka:
    x = 0
    y = 0

    def __init__(self, x, y):    # Konstruktor na osnovu zadatih x i y koordinata tačke
        self.x = x
        self.y = y

    def copy(self):              # Konstruktor na osnovu zadatog objekta Tacka (copy konstruktor)
        return copy.deepcopy(self)

    def pomeranje(self, x_pom, y_pom):   # Metod za pomeranje Tacke po x i y osi
        self.x = x_pom + self.x
        self.y = y_pom + self.y
        tacka = Tacka(self.x, self.y)
        return tacka

    def rastojanje(self):        # Metod za računanje rastojanja do zadate tačke
        x = self.x
        y = self.y
        self.rastojanje = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)
        return (self.rastojanje)



class Duz:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    tacka1 = Tacka(Tacka.x, Tacka.y)
    tacka2 = Tacka(Tacka.x, Tacka.y)

    @classmethod
    def duz(cls, tacka1, tacka2):    # Konstruktor na osnovu zadate početne i krajnje tačke duži
        cls.tacka1 = tacka1
        cls.tacka2 = tacka2
        return (cls(tacka1.x, tacka1.y, tacka2.x, tacka2.y))

    def __init__(self, x1, y1, x2, y2):    # Konstruktor na osnovu zadate x i y koordinate početne tačke i krajnje tačke
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def duzina(self):                     # Metod za računanje dužine duži
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        self.duzina = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return (self.duzina)