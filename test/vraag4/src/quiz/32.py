def verlaat_ploeg(naam, ploeg, dct):
    dct[ploeg].remove(naam)
    if len(dct[ploeg]) == 0:
        del dct[ploeg]
    return dct

def vervoegt_ploeg(naam, ploeg, dct):
    if ploeg in dct:
        if naam not in dct[ploeg]:
            dct[ploeg].append(naam)
    else:
        dct[ploeg] = [naam]
    return dct