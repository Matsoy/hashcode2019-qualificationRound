from operator import itemgetter
from scoring import countScoring

def combineTout(slides):
    scoreCombine=[]
    for photoP in range(len(slides)-1):
      # print(photoP)
      for photoE in range(photoP, len(slides)-1):
          score = countScoring(slides[photoP].tagList, slides[photoE].tagList)
          # print(slides[photoP].tagList)
          if (score > 2):
              scoreCombine.append((slides[photoP], slides[photoE], score))
    return scoreCombine


def sortList(scoreCombine):
    scoreCombine.sort(key=itemgetter(2), reverse=True)
    return scoreCombine
#res.append(scoreCombine[0])

#for r in scoreCombine:
def createSlideShow(slides, sortedArray, firstSlide):
    diapo=[]
    diapo.append(firstSlide)
    for i in range(100):
        # sortedArray.index(diapo[len(diapo)-1])
        search = diapo[len(diapo)-1]
        for emt in sortedArray:
            if(search in emt):
                if(emt[0] == search):
                    diapo.append(emt[0])
                else:
                    diapo.append(emt[1])
    return diapo
