from itertools import filterfalse
from operator  import itemgetter
from scoring   import count_score

def combine_all(slides):
    """
    :param slides:
    :return:
    """
    combined_scores=[]
    slides_ids_list = []
    for photo_a in range(len(slides)):
      slides_ids_list.append(slides[photo_a].id)
      # print(photo_a)
      for photo_b in range(photo_a+1, len(slides)):
          # print(photo_b)
          score = count_score(slides[photo_a].tags, slides[photo_b].tags)
          # print(slides[photo_a].tags_list)
          if (score >= 0):
              combined_scores.append((slides[photo_a], slides[photo_b], score))
    return (combined_scores, slides_ids_list)


def sort_list(combined_scores):
    """
    :param combined_scores:
    :return:
    """
    combined_scores.sort(key=itemgetter(2), reverse=True)
    return combined_scores
#res.append(combined_scores[0])


#for r in combined_scores:
def create_slideshow(sorted_array, first_slide, slides_ids_list, slideshow):
    """
    :param sorted_array:
    :param first_slide:
    :param slides_ids_list:
    :param slideshow:
    :return:                The slideshow
    """
    slides_to_pass = []

    for tup in sorted_array:
        if tup[0].id is not first_slide[1].id and tup[1].id is not first_slide[1].id:
            continue
        if tup[0].id is first_slide[1].id and tup[1].id in slides_ids_list:
            slideshow.append(tup[1])
            slides_to_pass = tup
            slides_ids_list.remove(tup[1].id)
        elif tup[1].id is first_slide[1].id and tup[0].id in slides_ids_list:
            slideshow.append(tup[0])
            slides_to_pass = (tup[1], tup[0], tup[2])
            slides_ids_list.remove(tup[0].id)
        else:
            continue
        create_slideshow(sorted_array, slides_to_pass, slides_ids_list, slideshow)
        break
    return slideshow


def determine(slideshow, search, emt):
    """
    :param slideshow:
    :param search:
    :param emt:
    """
    if(search in emt):
        if(emt[0] == search):
            slideshow.append(emt[0])
        else:
            slideshow.append(emt[1])
