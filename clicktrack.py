"""
Classes pour faire des clicktracks
"""
from typing import Self

import numpy as np
import pygame as pg
from time import sleep


# Il reste surtout à compléter les docstrings
# Les accents peuvent être sous la forme '21121' ou [2, 1, 1, 2, 1] ou le chiffre représente le niveua de l'accent
# 0 = pas de son, 1 = son nornal, 2 = son accentué, 3 = son encore plus accentué (par défault sur le premier temps)

# Ça pourrait être cool de mettre des sons différents pour les différents types d'accents.
class Measure:
    def __init__(self,
                 tempo: int | float = 60,
                 time_signature: str = '4/4',
                 accents: str | list | None = None
                 ):
        self.bpm = tempo
        self.time_signature = time_signature
        self.len, self.sub = self.time_signature.split('/')
        self.len, self.sub = int(self.len), int(self.sub)

        if isinstance(accents, list):
            self.accents = accents
        elif isinstance(accents, str):
            self.accents = [int(i) for i in list(accents)]
        elif accents is None:
            self.accents = [3]
            if self.len > 1:
                self.accents += [1 for _ in range(self.len - 1)]
        else:
            raise TypeError('accents must be a string, a list or a None object')
        if len(self.accents) != self.len:
            raise ValueError('The accents do not match the lenght of the measure')
    
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
        return f'Measure({self.time_signature}, {self.bpm} bpm)'
    
    def play(self):
        pathClick ='./metronome.wav'
        pg.mixer.init()
        click = pg.mixer.Sound(pathClick)

        dt = 60/(2**(np.log2(self.sub) - 2) * self.bpm)

        volumes = [0, 0.2, 0.7, 1]
        for i in self.accents:
            click.set_volume(volumes[i])
            click.play()
            sleep(dt)


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
        

        
