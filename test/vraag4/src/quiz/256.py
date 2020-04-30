def verlaat_ploeg(naam, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(naam)
    if not inschrijvingen[ploeg]:
        del inschrijvingen[ploeg]
    return inschrijvingen

def vervoegt_ploeg(naam, ploeg, inschrijvingen):
    if not ploeg in inschrijvingen:
        inschrijvingen[ploeg] = []
    if not naam in inschrijvingen[ploeg]:
        inschrijvingen[ploeg].append(naam)
    return inschrijvingen