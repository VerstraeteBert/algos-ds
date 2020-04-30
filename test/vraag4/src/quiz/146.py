def verlaat_ploeg(deelnemer, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(deelnemer)
    if len(inschrijvingen[ploeg]) == 0:
        del inschrijvingen[ploeg]
    return inschrijvingen

def vervoegt_ploeg(deelnemer, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        inschrijvingen[ploeg].append(deelnemer)
    else:
        inschrijvingen[ploeg] = [deelnemer]
    return inschrijvingen