def verlaat_ploeg(naam, ploeg, d):
    d[ploeg].remove(naam)
    if len(d[ploeg]) == 0:
        d.pop(ploeg)
    return d
def vervoegt_ploeg(naam, ploeg, d):
    if ploeg in d:
        d[ploeg].append(naam)
    else:
        d[ploeg] = [naam]
    return d