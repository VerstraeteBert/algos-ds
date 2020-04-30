def verlaat_ploeg(deelnemer, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(deelnemer)
    if not inschrijvingen[ploeg]:
        del inschrijvingen[ploeg]
    return inschrijvingen

def vervoegt_ploeg(deelnemer, ploeg, inschrijvingen):
    if not ploeg in inschrijvingen:
        inschrijvingen[ploeg]=[]
    inschrijvingen[ploeg].append(deelnemer)
    return inschrijvingen