def verlaat_ploeg(deel, ploeg, dic):
    dic[ploeg].remove(deel)
    if dic[ploeg] == []:
        del dic[ploeg]
    return dic
def vervoegt_ploeg(deel, ploeg, dic):
    if ploeg in dic:
        dic[ploeg].append(deel)
    else:
        dic[ploeg] = [deel]
    return dic