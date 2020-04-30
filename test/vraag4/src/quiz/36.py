def verlaat_ploeg(naam, ploeg, ploeglijst):
    ploeglijst[ploeg].remove(naam)
    if  not ploeglijst[ploeg]:
        del ploeglijst[ploeg]
    return ploeglijst

def vervoegt_ploeg(naam, ploeg, ploeglijst):
    if not ploeg in ploeglijst:
        ploeglijst[ploeg] = []
    if not naam in ploeglijst[ploeg]:
        ploeglijst[ploeg].append(naam)
    return ploeglijst