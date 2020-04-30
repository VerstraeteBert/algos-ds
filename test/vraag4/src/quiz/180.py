def verlaat_ploeg(naam,ploeg,dic):
    dic[ploeg].remove(naam)
    if len(dic[ploeg]) == 0:
       del dic[ploeg]
    return dic

def vervoegt_ploeg(naam,ploeg,dic):
    if ploeg in dic:
        dic[ploeg].append(naam)
    else:
        dic[ploeg] = [naam]
    return dic