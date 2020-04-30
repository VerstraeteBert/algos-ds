def verlaat_ploeg(naam, ploeg, dic):
    if naam in dic[ploeg]:
        dic[ploeg].remove(naam)
    if not dic[ploeg]:
        del dic[ploeg]
    return dic
    
def vervoegt_ploeg(naam, ploeg, dic):
    if ploeg in dic:
        if not naam in dic[ploeg]:
            dic[ploeg].append(naam)
    elif not ploeg in dic:
        dic[ploeg] = [naam]
    return dic