
def countingCommonTag(tagList1,tagList2):
    commonTag = 0
    if len(tagList1)<len(tagList2)
        tagL1 = tagList2
        tagL2 = tagList1
    else
        tagL1 = tagList1
        tagL2 = tagList2
    for tag1 in tagL1:
        for tag2 in tagL2:
            if tag1 == tag2
                commonTag+=1
    return commonTag

def countingTagS1(tagList1,tagList2):
    tagS1 = 0
    for tag1 in tagList1:
        for tag2 in tagList2:
            if not (tag1 == tag2)
                tagS1+=1
    return tagS1

def countingTagS2(tagList1,tagList2):
    tagS2 = 0
    for tag1 in tagList2:
        for tag2 in tagList1:
            if not (tag1 == tag2)
                tagS2+=1
    return tagS2

def countScoring(tagList1,tagList2):
    commonTag = countingCommonTag(tagList1,tagList2)
    tagS1 = countingTagS1(tagList1,tagList2)
    tagS2 = countingTagS2(tagList1,tagList2)
    return min(commonTag,tagS1,tagS2)