def verlaat_ploeg(naam, ploeg, d):
    l = d[ploeg]
    l = l.remove(naam)
    d.update()
    if not(d[ploeg]):
        d.pop(ploeg)
    return d
    


def vervoegt_ploeg(naam, ploeg, d):
    if ploeg in d:
        l = d[ploeg]
        l = l.append(naam)
    else:
        d[ploeg] = [naam]
    d.update()
    return d