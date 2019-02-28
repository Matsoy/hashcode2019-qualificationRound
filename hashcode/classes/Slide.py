
class Slide:
    def __init__(self,photo1,photo2):
        self.photo1 = photo1
        self.photo2 = photo2
        if self.photo2:
            self.tags = list(set(photo1.tagList+photo2.tagList))
        else:
            self.tags = photo1.tagList
