def count_common_tags(tags_list1, tags_list2):
    """
    :param tags_list1: The first list of tags
    :param tags_list2: The second list of tags
    :return:           The number of tags in common between these 2 slides
    """
    common_tags_cpt = 0
    tags_List1_tmp = tags_List2_tmp = []

    if len(tags_list1) < len(tags_list2):
        tags_List1_tmp = tags_list2
        tags_List2_tmp = tags_list1
    else:
        tags_List1_tmp = tags_list1
        tags_List2_tmp = tags_list2

    for tag1 in tags_List1_tmp:
        for tag2 in tags_List2_tmp:
            if tag1 == tag2:
                common_tags_cpt += 1

    return common_tags_cpt


def count_tags_s1(tags_list1, tags_list2):
    """
    :param tags_list1: The first list of tags
    :param tags_list2: The second list of tags
    :return:
    """
    tags_s1 = 0

    for tag1 in tags_list1:
        for tag2 in tags_list2:
            if not (tag1 == tag2):
                tags_s1+=1

    return tags_s1


def count_tags_s2(tags_list1, tags_list2):
    """
    :param tags_list1: The first list of tags
    :param tags_list2: The second list of tags
    :return:
    """
    tags_s2 = 0

    for tag1 in tags_list2:
        for tag2 in tags_list1:
            if not (tag1 == tag2):
                tags_s2+=1

    return tags_s2


def count_score(tags_list1, tags_list2):
    """
    :param tags_list1: The first list of tags
    :param tags_list2: The second list of tags
    :return:           The score obtained
    """
    common_tags_cpt = count_common_tags(tags_list1,tags_list2)
    tags_s1         = count_tags_s1    (tags_list1,tags_list2)
    tags_s2         = count_tags_s2    (tags_list1,tags_list2)

    return min(
        common_tags_cpt,
        tags_s1,
        tags_s2
    )
