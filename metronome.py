import pygame
import time
import fonctionsMetro as fM

pathMetro ='./metronome.wav'
pygame.mixer.init()                                                      #initialisation
sound = pygame.mixer.Sound(pathMetro)


tempo = int(input("Tempo voulu: "))                                      #Définition des variables
subdivision = int(input("Divisions voulue (4, 8 ou 16): "))
longueur = int(input("Nombre de temps par mesure: "))
# tempo = 120
# division = 4
# longueur = 7

accents = fM.accentDeBase(longueur)                                      #Initialisation de la liste de base à 1 accent
deltaT = fM.temps(tempo, subdivision)
accents = fM.patternAccent(longueur)                                     #Modification de la liste de base vers une liste a1 plusieurs accents
mesures = 2
i = 0

print(f'Pattern: {accents}')

print("Appuyez sur CTRL + C pour arrêter le métronome")
while True:                                                             #loop sur le nombre de mesure
    j = 0
    while j < longueur:                                                  #loop sur le nombre de temps
        if accents[j] == 1:
            sound.set_volume(1)                                          #Modification du volume pour les accents
            sound.play()           
            time.sleep(deltaT)

        else:
            sound.set_volume(0.2)
            sound.play()
            time.sleep(deltaT)
        j+=1
    i+=1