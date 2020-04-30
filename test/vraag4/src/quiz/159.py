#Quiz
def verlaat_ploeg(speler, ploeg, deelnemers):
    deelnemers[ploeg].remove(speler)
    if not deelnemers[ploeg]:
        del deelnemers[ploeg]
    return deelnemers



def vervoegt_ploeg(speler, ploeg, deelnemers):
    if not ploeg in deelnemers:
        deelnemers[ploeg] = []
    if not speler in deelnemers[ploeg]:
        deelnemers[ploeg].append(speler)
    return deelnemers
        