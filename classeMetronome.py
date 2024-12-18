import fonctionsMetro as fM

class Metronome:
    def __init__(self, tempo = 60, subdivision = 4):
        """On initialise un tempo de base en 60 bpm en 4/4"""
        self.tempo = tempo
        self.subdivision = subdivision
        self.intervalle = fM.temps(self.tempo, self.subdivision)
