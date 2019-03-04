from operator import itemgetter

class Slide:
    def __init__(self, photo1, photo2):
        """
        Constructor

        :param photo1: The first photo of the slide
        :param photo2: The second photo of the slide. Can be null
        """
        self.photo1 = photo1
        self.photo2 = photo2
        self.id     = str(photo1.id)

        if self.photo2 is not None:
            all_tags_with_duplicates = photo1.tags_list + photo2.tags_list
            all_tags_len             = len(all_tags_with_duplicates)
            self.tags                = list(set(all_tags_with_duplicates))
            self.duplication_ratio   = (1- (len(self.tags) / all_tags_len)) * 2
            self.nb_duplicates       = all_tags_len - len(self.tags)
            self.id                 += "_"+str(photo2.id)
        else:
            self.tags = photo1.tags_list
