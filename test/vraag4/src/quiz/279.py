def verlaat_ploeg(naam, ploeg, deelnemers):
    deelnemers[ploeg].remove(naam)
    if deelnemers[ploeg] == []:
        del deelnemers[ploeg]
    return deelnemers
    
def vervoegt_ploeg(naam, ploeg, deelnemers):
    if ploeg not in deelnemers:
        deelnemers[ploeg] = []
    if naam not in deelnemers[ploeg]:
        deelnemers[ploeg].append(naam)
    return deelnemers    