def verlaat_ploeg(naam, ploeg, dict):
    dict[ploeg].remove(naam)
    if dict[ploeg] == []:
        del dict[ploeg]

    return dict

def vervoegt_ploeg(naam, ploeg, dict):
    if ploeg in dict:
        dict[ploeg] = dict[ploeg] + [naam]
    else:
        dict[ploeg] = [naam]

    return dict
