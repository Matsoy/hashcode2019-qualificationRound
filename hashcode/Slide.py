from operator import itemgetter

nbPhoto=100;
slides # list de photos
res=[]


def combineTout(slides):
    scoreCombine=[]
    for photoP in range(len(slides)-1):
      for photoE in range(photoP, len(slides)-1):
          score = getScorePhoto()
          scoreCombine.append((slides[photoP], slides[photoE], res)
    return scoreCombine



scoreCombine.sort(key=itemgetter(2), reverse=False)
res.append(scoreCombine[0])

for r in scoreCombine:
