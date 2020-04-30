def verlaat_ploeg(deelnemer, ploeg, d):
    d[ploeg].remove(deelnemer)
    if d[ploeg]==[]:
        del d[ploeg]
    return d

def vervoegt_ploeg(deelnemer, ploeg, d):
    if ploeg in d:
        d[ploeg].append(deelnemer)
    else:
        d[ploeg]=[deelnemer]
    return d