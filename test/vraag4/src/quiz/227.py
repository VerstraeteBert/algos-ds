def verlaat_ploeg(naam, ploeg, dict_ingeschreven):
    dict_ingeschreven[ploeg].remove(naam)
    if dict_ingeschreven[ploeg] == []:
        del dict_ingeschreven[ploeg]
    return dict_ingeschreven


def vervoegt_ploeg(naam, ploeg, dict_ingeschreven):
    if ploeg in dict_ingeschreven:
        if naam not in dict_ingeschreven[ploeg]:
            dict_ingeschreven[ploeg].append(naam)
    else:
        dict_ingeschreven[ploeg] = [naam]
    return dict_ingeschreven

