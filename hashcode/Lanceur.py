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
                del photoParams[-1]
                self.listePhotos.append(Photo(i, photoParams[2:], photoParams[0]))

    def fichierSortie(self, slides):
        print("fichierSortie")
        fichier = open("outputs/"+self.fichier+"_"+now.second + ".out", "w")

        fichier.write(str(len(slides))+"\n")
        for slide in slides:
            fichier.write(str(slide.photo1))
            if slide.photo1 is not None:
                fichier.write(" "+str(slide.photo2))
            fichier.write("\n")

        fichier.close()


    def lancerSimulation(self) :
        """
        Lancement de la simulation
        """



# initialisation d'un objet de type Lanceur
print("==============> Debut simulation")
l = Lanceur(sys.argv[1])
print("==============> Fin simulation")

a = Algo(l)

