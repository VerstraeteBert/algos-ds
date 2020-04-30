def verlaat_ploeg(verlater, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(verlater)
    if not inschrijvingen[ploeg]:
        del inschrijvingen[ploeg]
    return inschrijvingen
def vervoegt_ploeg(naam, ploeg, deelnemers):
    if not ploeg in deelnemers:
        deelnemers[ploeg] = []
    if not naam in deelnemers[ploeg]:
        deelnemers[ploeg].append(naam)
    return deelnemers    
