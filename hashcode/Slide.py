from operator import itemgetter

class Slide:
    def __init__(self,photo1,photo2):
        self.photo1 = photo1
        self.photo2 = photo2
        print("test")
        if self.photo2 is not None:
            print(photo1.tagList,photo2.tagList)
            self.tags = list(set(photo1.tagList+photo2.tagList))
            print(self.tags)
        else:
            self.t = "tutu"
            self.tags = photo1.tagList
