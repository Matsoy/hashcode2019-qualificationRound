# from main import main
import copy
import math
import time
import sys
from   slides_utilities       import *
from   horizontal_combination import *
from   scoring                import count_score
from   slide                  import Slide

class Algo:
    def __init__(self, main):
        """
        Constructor

        :param main: Main instance that contains attributes from the input file
        """
        self.main = main
        print(str(len(main.photos_list)) + " photos")
        self.generate_vertical_pairs()
        # for o in self.slides_list:
            # print(o.id)
        (combined_score, slides_ids_list) = combine_all(self.slides_list)
        combined_score.sort(
            key=itemgetter(2),
            reverse=True
        )
        slides_ids_list.remove(combined_score[0][0].id)
        slides_ids_list.remove(combined_score[0][1].id)
        slideshow = create_slideshow(
            combined_score,
            combined_score[0],
            slides_ids_list,
            [
                combined_score[0][0],
                combined_score[0][1]
            ]
        )
        # res = sort_list(combined_score)
        # for i in slideshow:
        #     print(i)
        #Get score
        previous_slide = None
        score = 0

        for slide in slideshow:
            if previous_slide is not None:
                score = score + count_score(previous_slide.tags,slide.tags)
            previous_slide = slide
        print("score : ",score)
        self.main.write_output_file(slideshow, score)


    def generate_vertical_pairs(self):
        """
        """
        self.slides_list = []
        #all_pairs = [None]*len(self.main.photos_list)
        all_vertical_ids = []
        slides_list2 = []

        for photo1 in self.main.photos_list :
            if photo1.orientation is 'H':
                self.slides_list.append(Slide(photo1,None))
                continue
            all_vertical_ids.append(photo1.id)
            #all_pairs[photo1.id] = [None]*len(self.main.photos_list)
            for photo2 in self.main.photos_list :
                if (
                        photo2.orientation is not 'H' 
                    and photo1.id is not photo2.id
                ):
                    slide = Slide(photo1,photo2)
                    #all_pairs[photo1.id][photo2.id] = slide
                    slides_list2.append(slide)
        #All horizontal slide are created
        #need now to select all vertical pair
        slides_to_return = naive_combination(slides_list2,all_vertical_ids)

        for slide in slides_to_return:
            self.slides_list.append(slide)
