def verlaat_ploeg(naam, ploeg, dic):
    dic[ploeg].remove(naam)
    if not dic[ploeg]:
        del dic[ploeg]
    return dic

def vervoegt_ploeg(naam, ploeg, dic):
    if not ploeg in dic:
        dic[ploeg] = []
    if not naam in dic[ploeg]:
        dic[ploeg].append(naam)
    return dic