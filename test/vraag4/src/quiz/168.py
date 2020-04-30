def verlaat_ploeg(naam, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(naam)
    if not inschrijvingen[ploeg]:
        del inschrijvingen[ploeg]
    return inschrijvingen

def vervoeg_ploeg(naam, ploeg, inschrijvingen):
    if not ploeg in inschrijvingen:
        inschrijvingen[ploeg] = []
    if ploeg in inschrijvingen:
        inschrijvingen[ploeg].append(naam)
    return inschrijvingen
    