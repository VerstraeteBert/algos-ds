def verlaat_ploeg(speler, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(speler)
    if not inschrijvingen[ploeg]:
        del inschrijvingen[ploeg]
    return inschrijvingen


def vervoegt_ploeg(speler, ploeg, inschrijvingen):
    if ploeg not in inschrijvingen:
        inschrijvingen[ploeg] = []
    if speler not in inschrijvingen[ploeg]:
        inschrijvingen[ploeg].append(speler)
    return inschrijvingen