# -*- coding: utf-8 -*-

from datetime import date

class Osoba():

    def __init__(self, ime, prezime, y, m, d, adresa):       # Konstruktor
        self.ime = ime
        self.prezime = prezime
        self.datum = date(y,m,d)
        self.adresa = adresa


class Dzak(Osoba):
    godina = 0

    def __init__(self,ime, prezime, y, m, d, adresa, skola, odd, godina):    # Konstruktor
        Osoba.__init__(self, ime, prezime, y, m, d, adresa)
        self.skola = skola
        self.odd = odd
        self.godina = godina

    def info(self):               # Informacije o đaku
        print "\nĐak", self.ime, self.prezime, "datum rođenja", self.datum, "kucna adresa", self.adresa,\
            "upisao je", self.godina, "godinu u odeljenje", self.odd, "u školi", self.skola
        return ""

    def odelenje(self):           # Informacija u razred škole đak trenutno pohađa
        print "Đak ide u", self.odd, "odelenje"

    def obnovio(self):            # Metod koji računa da li je možda obnovio neku godinu tokom školovanja
        if (self.godina > 1):
            print "Đak je obnovio godinu po", self.godina, "put"
        else:
            return 0


class Zaposlen(Osoba):
    dani = []                       # Lista ukupan broj dani kojih je radio
    radio = []

    def __init__(self, ime, prezime, y, m, d, adresa, kompanija, department):    # Konstruktor
        Osoba.__init__(self, ime, prezime, y, m, d, adresa)
        self.kompanija = kompanija
        self.department = department

    @classmethod                 # Metod koji dodaje periode u kome je zaposlen radio
    def radi(cls, y, m, d, y1, m1, d1):
        cls.poceo = date(y,m,d)
        cls.prekinuo = date(y1,m1,d1)
        Zaposlen.radio.append(cls.poceo)
        Zaposlen.radio.append(cls.prekinuo)
        ukupno = (cls.prekinuo - cls.poceo).days + 1
        Zaposlen.radio.append(ukupno)
        Zaposlen.dani.append(ukupno)

    def info(self):                             # Informacije o zaposlen
        print "\nZaposlen", self.ime, self.prezime, "datum rođenja", self.datum, "kucna adresa", self.adresa, \
            "radi u", self.kompanija, "department", self.department, "\n"
        return ""

    def staz(self):                # Metod koji računa ukupan broj meseca kojih je radio
        dani = self.dani
        self.meseci = float(sum(dani) / 30.0)
        print "Zaposlenje bio u radnom odnosu u periodu od", Zaposlen.radio
        print "Zaposljen ima staz:", self.meseci, "meseci"