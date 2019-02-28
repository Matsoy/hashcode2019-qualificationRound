# from Lanceur import Lanceur
import copy
import math
import time
import sys
from fctSlides import *

from Slide import Slide

class Algo:
    def __init__(self,lanceur):
        self.lanceur = lanceur

        print(len(lanceur.listePhotos))
        self.lanceur = lanceur
        self.generateVerticalPair()
        # for o in self.listeSlides:
            # print(o.id)
        (scoreCombine, listIdSlide) = combineTout(self.listeSlides)
        scoreCombine.sort(key=itemgetter(2), reverse=True)
        listIdSlide.remove(scoreCombine[0][0].id)
        listIdSlide.remove(scoreCombine[0][1].id)
        diapo = createSlideShow(scoreCombine, scoreCombine[0],listIdSlide,[scoreCombine[0][0],scoreCombine[0][1]])
        # res = sortList(scoreCombine)
        # for i in diapo:
        #     print(i)
        self.lanceur.fichierSortie(diapo)


    def generateVerticalPair(self):
        self.listeSlides = []
        #allPair = [None]*len(self.lanceur.listePhotos)
        allVerticalId = []
        listSlide = []
        for photo1 in self.lanceur.listePhotos :
            if photo1.orientation is 'H':
                self.listeSlides.append(Slide(photo1,None))
                continue
            allVerticalId.append(photo1.id)
            #allPair[photo1.id] = [None]*len(self.lanceur.listePhotos)
            for photo2 in self.lanceur.listePhotos :
                if photo2.orientation is not 'H' and photo1.id is not photo2.id:
                    slide = Slide(photo1,photo2)
                    #allPair[photo1.id][photo2.id] = slide
                    listSlide.append(slide)
        #All horizontal slide are created
        #need now to select all vertical pair
        listSlide.sort(key=lambda slide: len(slide.tags),reverse=True)

        for slide in listSlide:
            if slide.photo1.id in allVerticalId and slide.photo2.id in allVerticalId:
                self.listeSlides.append(slide)
                allVerticalId.remove(slide.photo1.id)
                allVerticalId.remove(slide.photo2.id)
