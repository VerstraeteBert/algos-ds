def verlaat_ploeg(naam, ploeg, namenlijst):
    if len(namenlijst[ploeg]) > 1:
        namenlijst[ploeg].remove(naam)
    else:
        namenlijst.pop(ploeg)
    return namenlijst

def vervoegt_ploeg(naam, ploeg, namenlijst):
    if ploeg in namenlijst:
        namenlijst[ploeg].append(naam)
    else:
        namenlijst[ploeg] = [naam]
    return namenlijst