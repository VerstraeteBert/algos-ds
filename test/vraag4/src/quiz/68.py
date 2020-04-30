def verlaat_ploeg(naam,ploeg,d):
    lijst = d[ploeg]
    lijst = lijst.remove(naam)
    if not d[ploeg]:
        del d[ploeg]
    return d
    
def vervoegt_ploeg(naam, ploeg, deelnemers):
    if not ploeg in deelnemers:
        deelnemers[ploeg] = []
    if not naam in deelnemers[ploeg]:
        deelnemers[ploeg].append(naam)
    return deelnemers    