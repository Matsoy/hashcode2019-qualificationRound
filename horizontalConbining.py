

from Slide import Slide

def conbiningNaif(listSlide,allVerticalId):
    returnSlide = []
    listSlide.sort(key=lambda slide: len(slide.tags),reverse=True)
    for slide in listSlide:
        if slide.photo1.id in allVerticalId and slide.photo2.id in allVerticalId:
            returnSlide.append(slide)
            allVerticalId.remove(slide.photo1.id)
            allVerticalId.remove(slide.photo2.id)
    return returnSlide

def conbiningImproved(listSlide,allVerticalId,allPair):
    returnSlide = []
    listSlide2 = listSlide.copy()
    listSlide2.sort(key=lambda slide: len(slide.tags),reverse=True)
    listSlide.sort(key=lambda slide: (slide.duplicationRatio),reverse=True)
    for slide in listSlide:
        if slide.photo1.id in allVerticalId and slide.photo2.id in allVerticalId:
            slided = -1
            for slide2 in allPair[slide.photo1.id]:
                if slide2.photo2.id in allVerticalId and slide2.photo1.id is slide.photo1.id:
                    returnSlide.append(slide2)
                    allVerticalId.remove(slide2.photo1.id)
                    allVerticalId.remove(slide2.photo2.id)
                    slided = slide2.photo2.id
            for slide2 in allPair[slide.photo2.id]:
                if slide2.photo2.id in allVerticalId and slide2.photo1.id is slide.photo1.id and slide2.photo2.id is not slided:
                    returnSlide.append(slide2)
                    allVerticalId.remove(slide2.photo1.id)
                    allVerticalId.remove(slide2.photo2.id)
    return returnSlide
