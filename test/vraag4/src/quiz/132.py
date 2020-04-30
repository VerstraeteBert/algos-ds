def verlaat_ploeg(naam, ploeg, dictionarie):
    dictionarie[ploeg].remove(naam)
    if dictionarie[ploeg] == []:
        del dictionarie[ploeg]
    return dictionarie

def vervoegt_ploeg(naam, ploeg, dictionarie):
    if ploeg in dictionarie:
        dictionarie[ploeg].append(naam)
    else:
        dictionarie[ploeg] = [naam]
    return dictionarie