"""
Classes pour faire des clicktracks
"""
from typing import Self

import classeMetronome as metro


class Measure:
    def __init__(self, tempo: int | float=60, time_signature='4/4', accents='4'):
        self.bpm = tempo
        self.len, self.sub = time_signature.split('/')
        self.accents = accents
    
    def __add__(self, other: Self | 'ClickTrack'):
        measure = [self]
        if isinstance(other, ClickTrack):
            new_measures = measure + other.measures
        elif isinstance(other, Measure):
            new_measures = measure + [other]
        else:
            raise TypeError
        return ClickTrack(new_measures)

    def __mul__(self, rep: int):
        if rep <= 0:
            raise ValueError
        return ClickTrack([self] * rep)
    
    def __repr__(self):
        return f'Measure({self.len}/{self.sub}, {self.bpm} bpm)'
    
    def play(self):
        pass


class ClickTrack:
    def __init__(self, measures: list=[]):
        self.measures = measures

    def __add__(self, other: Self | Measure):
        if isinstance(other, ClickTrack):
            new_measures = self.measures + other.measures
        elif isinstance(other, Measure):
            new_measures = self.measures + [other]
        else:
            raise TypeError
        return ClickTrack(new_measures)
    
    def __mul__(self, rep):
        if rep <= 0:
            raise ValueError
        return ClickTrack(self.measures * rep)
    
    def __getitem__(self, i):
        return self.measures[i]
    
    def __repr__(self):
        return f"ClickTrack({repr(self.measures)})"

    def play(self):
        for measure in self.measures:
            measure.play()

    def ecrire(nomTrack):
        stop = 0
        while stop == 0:
            fichier = open(nomTrack, "x")
            tot = int(input("Nombre de mesures désiré pour cette section: "))
            tempo = int(input("Tempo désiré: "))
            while i < tot:
                len = input("Nombre de temps dans la mesure: ")
                sub = input("Subdivisions: ")
                nb = int(input("Nombre désiré de mesures de ce type: "))
                j = 0
                fichier.write(f"t={tempo}" + " ")
                while j < nb:
                    fichier.write(f"{len}/{sub}" + " ")
                    j += 1
                i += 1
            fichier.write("\n")
            stop = int(input("Voulez-vous continuer à écrire d'autres sections? (Entrez 0 pour oui, 1 pour non)"))

        fichier.close()

    def lire(self, nomTrack):
        pass
        

        
