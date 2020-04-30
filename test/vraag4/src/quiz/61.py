def verlaat_ploeg(naam, ploeg, d):
    namen = d[ploeg]
    for naam1 in namen:
        if naam == naam1:
            d[ploeg].remove(naam)
        if d[ploeg] == []:
            del d[ploeg]
    return d

def vervoegt_ploeg(naam, ploeg, d):
    try:
        d[ploeg].append(naam)
        return d
    except KeyError:
        d[ploeg] = [naam]
        return d
        