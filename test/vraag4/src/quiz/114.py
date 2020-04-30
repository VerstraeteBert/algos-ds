def verlaat_ploeg(naam, ploeg, deelnemers):
    deelnemers[ploeg].remove(naam)
    if not deelnemers[ploeg]:
        del deelnemers[ploeg]
    return deelnemers
    
def vervoegt_ploeg(naam, ploeg, deelnemers):
    if not ploeg in deelnemers:
        deelnemers[ploeg] = []
    if not naam in deelnemers[ploeg]:
        deelnemers[ploeg].append(naam)
    return deelnemers  