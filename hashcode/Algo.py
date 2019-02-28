# from Lanceur import Lanceur
import copy
import math
import time
import sys
from fctSlides import *

class Algo:
    def __init__(self,lanceur):
        self.lanceur = lanceur

        print(len(lanceur.listePhotos))
        scoreCombine = combineTout(lanceur.listePhotos)
        scoreCombine.sort(key=itemgetter(2), reverse=True)
        diapo = createSlideShow(lanceur.listePhotos, scoreCombine, scoreCombine[0][0])
        # res = sortList(scoreCombine)
        # for i in diapo:
        #     print(i)
        self.lanceur.fichierSortie(diapo)
