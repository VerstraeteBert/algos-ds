def vervoegt_ploeg(naam, ploeg, dict):
    if ploeg in dict:
        if naam not in dict[ploeg]:
            dict[ploeg].append(naam)
    else:
        dict[ploeg] = [naam]
    return dict

def verlaat_ploeg(naam, ploeg, dict):
    lst = dict[ploeg]
    lst.remove(naam)
    if not lst:
        del dict[ploeg]
    else:
        dict[ploeg] = lst
    return dict
    