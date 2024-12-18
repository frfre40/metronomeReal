import numpy as np

""" Fonctions de base """
def temps(tempo, subdivision):
### Cette fonction calcule l'intervalle de temps entre chaque note ###

    n = np.log2(subdivision)
    tempo = 2**(n - 2) * tempo
    return 60/tempo


def accentDeBase(nombre):
### Cette fonction retourne une liste avec un accent uniquement sur le premier temps ###

    liste = []
    for i in range(nombre):
        if i == 0:
            liste.append(1)
        else:
            liste.append(0)
    return liste

def patternAccent(longueur):
### Cette fonction retourne une liste avec des accents au positions demandées ###

    nbTemps = longueur                                          #Définition du nombre de temps dans une mesure

    divisions = input("Comment voulez-vous diviser la mesure (groupes de 1, 2 ou 3)?: ")  #Définition du pattern d'accents. Le somme doit ABSOLUMENT être le nombre de temps
    listeDivisions = divisions.split(',')                                              #Séparation des accents dans un liste
    for i in range(len(listeDivisions)):
        listeDivisions[i] = int(listeDivisions[i])                                     #Conversion des élément de listeDivisions de string à int

    pattern = accentDeBase(nbTemps)                                                    #Initialisation d'une liste avec un accent sur le 1
                                                                                       #basé sur le nombre de temps
    position = 0
    for i in range(0, len(listeDivisions) - 1):                                        #Assignation de la valeur 1 aux positions demandées                   
        position += listeDivisions[i]                                                  #-->La boucle va directement à la position du 2e accent
        pattern[position] = 1                                                          #et ignore le dernier élément de la liste d'accents car il est placé "naturellement"
                                                                                       #lorsque l'avant dernier est placé
    return pattern

""" Gestion de problèmes et d'utilisateurs caves """
# duree = 0
# for element in divisions:
#     duree += element
# if duree != nbTemps:
#     divisions = input(f"Durée entrée est inférieure au nombre de temps (Vous avez entré {duree} à la place de {nbTemps}). Veuillez ajouter : ")


# echo "# Metronome" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/frfre40/Metronome.git
# git push -u origin main