from operator import itemgetter

class Slide:
    def __init__(self,photo1,photo2):
        self.photo1 = photo1
        self.photo2 = photo2
        self.id=str(photo1.id)
        if self.photo2 is not None:
            allTagsWithDouble = photo1.tagList+photo2.tagList
            lenAllTags = len(allTagsWithDouble)
            self.tags = list(set(allTagsWithDouble))
            self.duplicationRatio = (1-(len(self.tags)/lenAllTags))*2
            self.nbDuplicate = lenAllTags-len(self.tags)
            self.id+="_"+str(photo2.id)
        else:
            self.tags = photo1.tagList
