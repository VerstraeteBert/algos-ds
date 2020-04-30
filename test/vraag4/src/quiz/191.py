def verlaat_ploeg(naam, ploeg, deelnemers):
    deelnemers[ploeg].remove(naam)
    if not deelnemers[ploeg]:
        del deelnemers[ploeg]
    return deelnemers

def vervoegt_ploeg(naam, ploeg, deelnemers):
    if ploeg not in deelnemers:
        deelnemers[ploeg] = [naam]
    if naam in deelnemers[ploeg]:
        return deelnemers
    else:
        deelnemers[ploeg].append(naam)
    return deelnemers


