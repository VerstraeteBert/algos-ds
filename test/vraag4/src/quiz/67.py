def verlaat_ploeg(naam, ploeg, dic):
    lijst = dic[ploeg]
    lijst.remove(naam)
    if not lijst:
        dic.pop(ploeg)
    return dic

def vervoegt_ploeg(naam, ploeg, dic):
    if ploeg in dic:
        lijst = dic[ploeg]
        lijst.append(naam)
    else:
        dic[ploeg] = [naam]
    return dic