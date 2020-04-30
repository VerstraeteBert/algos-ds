def verlaat_ploeg(naam, ploeg, insch):
    # print(insch)  # test
    leden = insch[ploeg]
    leden.remove(naam)
    insch[ploeg] = leden
    if len(insch[ploeg]) == 0:
        del insch[ploeg]
    return insch

def vervoegt_ploeg(naam, ploeg, insch):
    # print(insch)  # test
    leden = []
    if ploeg in insch:
        leden = insch[ploeg]
        leden.append(naam)
        insch[ploeg] = leden
    else:
        leden.append(naam)
        insch[ploeg] = leden
    return insch