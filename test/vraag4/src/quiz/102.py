def verlaat_ploeg(naam, ploeg, dict):
    leden = dict[ploeg]
    leden.remove(naam)
    dict[ploeg] = leden
    if dict[ploeg] == []:
        del dict[ploeg]
    return dict


def vervoegt_ploeg(naam, ploeg, dict):
    try:
        leden = dict[ploeg]
        leden.append(naam)
        dict[ploeg] = leden
    except KeyError:
        dict[ploeg] = [naam]
    return dict