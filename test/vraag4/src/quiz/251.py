def verlaat_ploeg(naam, ploeg, inschrijvingen):

    if ploeg in inschrijvingen:
        inschrijvingen[ploeg].remove(naam)
    if not inschrijvingen[ploeg]:
        del inschrijvingen[ploeg]
    
    return inschrijvingen

def vervoegt_ploeg(naam, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        inschrijvingen[ploeg].append(naam)
    if not ploeg in inschrijvingen:
        inschrijvingen[ploeg] = [naam]
    return inschrijvingen