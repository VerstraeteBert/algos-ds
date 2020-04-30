def verlaat_ploeg(naam, ploeg, bibl):
    for groep in bibl:
        if len(bibl[ploeg]) == 1:
            del bibl[ploeg]
            break
        else:
            if naam in bibl[ploeg]:
                bibl[ploeg].remove(naam)
    return bibl


def vervoegt_ploeg(naam, ploeg, bibl):
    if ploeg not in bibl:
        bibl[ploeg] = []
    for groep in bibl:
        if groep == ploeg:
            bibl[ploeg].append(naam)
    return bibl