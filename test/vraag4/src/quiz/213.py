def verlaat_ploeg(deelnemer, ploeg, inschrijvingen):
    deelnemers = inschrijvingen[ploeg]
    deelnemers.remove(deelnemer)
    inschrijvingen[ploeg] = deelnemers
    if inschrijvingen[ploeg] == []:
        del inschrijvingen[ploeg]
    return inschrijvingen

def vervoegt_ploeg(deelnemer, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        deelnemers = inschrijvingen[ploeg]
        deelnemers = deelnemers.append(deelnemer)
    else:
        inschrijvingen[ploeg] = [deelnemer]
    return inschrijvingen
