from slide import Slide

def naive_combination(slides_list, all_vertical_ids):
    """
    :param slides_list:
    :param all_vertical_ids: q
    :return:                 Slides list
    """
    slides_to_return = []
    slides_list.sort(
        key=lambda slide: len(slide.tags),
        reverse=True
    )

    for slide in slides_list:
        if (
                slide.photo1.id in all_vertical_ids 
            and slide.photo2.id in all_vertical_ids
        ):
            slides_to_return.append(slide)
            all_vertical_ids.remove(slide.photo1.id)
            all_vertical_ids.remove(slide.photo2.id)

    return slides_to_return


def improved_combination(slides_list, all_vertical_ids, all_pairs):
    """
    :param slides_list:
    :param all_vertical_ids:
    :param all_pairs:
    :return:                 Slides list
    """
    slides_to_return = []
    slides_list2     = slides_list.copy()
    slides_list2.sort(
        key=lambda slide: len(slide.tags),
        reverse=True
    )
    slides_list.sort(
        key=lambda slide: slide.duplication_ratio,
        reverse=True
    )
    
    for slide in slides_list:
        if (
                slide.photo1.id in all_vertical_ids 
            and slide.photo2.id in all_vertical_ids
        ):
            slided = -1
            for slide2 in all_pairs[slide.photo1.id]:
                if (
                        slide2.photo2.id in all_vertical_ids 
                    and slide2.photo1.id is slide.photo1.id
                ):
                    slides_to_return.append(slide2)
                    all_vertical_ids.remove(slide2.photo1.id)
                    all_vertical_ids.remove(slide2.photo2.id)
                    slided = slide2.photo2.id
            for slide2 in all_pairs[slide.photo2.id]:
                if (
                        slide2.photo2.id in all_vertical_ids 
                    and slide2.photo1.id is slide.photo1.id 
                    and slide2.photo2.id is not slided
                ):
                    slides_to_return.append(slide2)
                    all_vertical_ids.remove(slide2.photo1.id)
                    all_vertical_ids.remove(slide2.photo2.id)
                    
    return slides_to_return
