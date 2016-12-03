# -*- coding: utf-8 -*-

class Inzenjer():
    def __init__(self, ime, prezime, jmbg, licenca):
        self._ime = ime
        self._prezime = prezime
        self._jmbg = jmbg
        self._licenca = licenca

    @property                  # Odgovarajuće getter i setter metode
    def ime(self):
        return self._ime

    @property
    def prezime(self):
        return self._prezime

    @property
    def jmbg(self):
        return self._jmbg

    @property
    def licenca(self):
        return self._licenca

    @ime.setter
    def ime(self, ime):
        self._ime = ime

    @prezime.setter
    def prezime(self, prezime):
        self._prezime = prezime

    @jmbg.setter
    def jmbg(self, jmbg):
        self._jmbg = jmbg

    @licenca.setter
    def licenca(self, licenca):
        self._licenca = licenca

    def info(self):                   # Ispis informacija o inženjeru
        print "Inženjer:", self.ime, self.prezime, ", JMBG:", self.jmbg
        return ""

class GeodetskiInzenjer(Inzenjer):
    def __init__(self,ime, prezime, jmbg, licenca, staz):
        Inzenjer.__init__(self, ime, prezime, jmbg, licenca)
        self._staz = staz

    @property                    # Odgovarajuće getter i setter metode
    def staz(self):
        return self._staz

    @staz.setter
    def staz(self, staz):
        self._staz = staz

    def info2(self):             # Ispis informacija o geodetskom inženjeru
        print self.info() + "Broj godina radnog staža je:", self.staz
        return ""

    def imaLicencu(self):         # Ispisi informacije o licenci ukoliko je ima
        if self.licenca is not None:
            print "Broj licence je: ", self.licenca
        else:
            print "Inženjer nema licencu"
        return ""

class ElektroInzenjer(Inzenjer):
    def __init__(self, ime, prezime, jmbg, licenca, projekte):
        Inzenjer.__init__(self, ime, prezime, jmbg, licenca)
        self._projekte = projekte

    @property                      # Odgovarajuće getter i setter metode
    def projekte(self):
        return self._projekte

    @projekte.setter
    def projekte(self, projekte):
        self._projekte = projekte

    def info2(self):              # Ispis svih informacija o inženjeru elektrotehnike
        print self.info() + "Broj projekata na kojima je do sada radio je:", self.projekte
        return ""

    def imaLicencu(self):         # Ispisi informacije o licenci ukoliko je ima
        if self.licenca is not None:
            print "Broj licence je: ", self.licenca
        else:
            print "Inženjer nema licencu"
        return ""

