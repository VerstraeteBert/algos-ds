def verlaat_ploeg(naam, ploeg, dic):
    lijst = dic[ploeg]
    lijst.remove(naam)
    if lijst == []:
        del dic[ploeg]
    else:
        dic[ploeg] = lijst
    return dic
    
    
def vervoegt_ploeg(naam, ploeg, dic):
    if ploeg in dic.keys():
        lijst = dic[ploeg]
        lijst.append(naam)
        dic[ploeg] = lijst
    else:
        dic[ploeg] = [naam]
    return dic