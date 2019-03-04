from itertools import filterfalse
from operator import itemgetter
from scoring import countScoring

def combineTout(slides):
    scoreCombine=[]
    listIdSlide = []
    for photoP in range(len(slides)):
      listIdSlide.append(slides[photoP].id)
      # print(photoP)
      for photoE in range(photoP+1, len(slides)):
          # print(photoE)
          score = countScoring(slides[photoP].tags, slides[photoE].tags)
          # print(slides[photoP].tagList)
          if (score >= 0):
              scoreCombine.append((slides[photoP], slides[photoE], score))
    return (scoreCombine,listIdSlide)


def sortList(scoreCombine):
    scoreCombine.sort(key=itemgetter(2), reverse=True)
    return scoreCombine
#res.append(scoreCombine[0])

#for r in scoreCombine:
def createSlideShow(sortedArray, firstSlide,listIdSlide,diapo):
    slidesPasse=[]

    for tup in sortedArray:
        if tup[0].id is not firstSlide[1].id and tup[1].id is not firstSlide[1].id:
            continue
        if tup[0].id is firstSlide[1].id and tup[1].id in listIdSlide:
            diapo.append(tup[1])
            slideToPass = tup
            listIdSlide.remove(tup[1].id)
        elif tup[1].id is firstSlide[1].id and tup[0].id in listIdSlide:
            diapo.append(tup[0])
            slideToPass = (tup[1],tup[0],tup[2])
            listIdSlide.remove(tup[0].id)
        else:
            continue
        createSlideShow(sortedArray, slideToPass,listIdSlide,diapo)
        break
    return diapo

def determine(diapo, search, emt):
    if(search in emt):
        if(emt[0] == search):
            diapo.append(emt[0])
        else:
            diapo.append(emt[1])
