def verlaat_ploeg(naam, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(naam)
    if inschrijvingen[ploeg] == []:
        del inschrijvingen[ploeg]
    return inschrijvingen

def vervoegt_ploeg(naam, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        if naam not in inschrijvingen[ploeg]:
            inschrijvingen[ploeg].append(naam)
    else:
        inschrijvingen[ploeg] = [naam]
    return inschrijvingen