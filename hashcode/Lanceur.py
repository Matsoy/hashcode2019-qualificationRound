# from Temps import Temps
# from Collection import Collection
from Photo import Photo
from Algo import Algo
import copy
import math
import time
import sys

class Lanceur:
    def __init__(self,fichier):

    
        self.fichier = "./inputs/" + fichier + ".txt"
        print("fichier",self.fichier)
        self.listePhotos = []
        
        self.lectureFichier()
        # self.lancerSimulation()

    def lectureFichier(self):
        print("lectureFichier")


        with open(self.fichier,'r') as f:
            nbPhotos = int(f.readline())
            for i in range(0, nbPhotos):
                photoParams = f.readline().split(" ")
                self.listePhotos.append(Photo(i, photoParams[2:], photoParams[0]))

    # def fichierSortie(self):
    #     print("fichierSortie")


    #     # Pour eviter les duplications dans le fichier de sortie, dans le cas ou une seule prise de photo a permis d'avancer plusieurs collections
    #     listePointsPris = []
    #     # Parcours de toutes les coordonnees des collections validees
    #     for collect in self.listeCollectionValidee:
    #         for coord in collect.listeCoordonneesReussies:
    #             # Si les coordonnees du point ne sont pas dans listePointsPris, alors on les rajoute a la liste
    #             if not coord in listePointsPris:
    #                 listePointsPris.append(coord)

    #     fichier = open("fichierSortie.out", "w")
    #     # Ecriture du nombre total de coordonnees
    #     fichier.write(str(len(listePointsPris))+"\n")
    #     for coord in listePointsPris:
    #         fichier.write(str(coord[0])+ " " + str(coord[1]) + " " + str(coord[2]) + " " + str(coord[3]) + "\n")
    #     fichier.close()


    def lancerSimulation(self) :
        """
        Lancement de la simulation
        """



# initialisation d'un objet de type Lanceur
print("==============> Debut simulation")
l = Lanceur(sys.argv[1])
print("==============> Fin simulation")

a = Algo(l)

