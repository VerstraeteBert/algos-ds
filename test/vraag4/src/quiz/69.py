def verlaat_ploeg(persoon, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(persoon)
    if inschrijvingen[ploeg] == []:
        del inschrijvingen[ploeg]
    return inschrijvingen

def vervoegt_ploeg(persoon, ploeg, inschrijvingen):
    if ploeg not in inschrijvingen:
        inschrijvingen[ploeg] = [persoon]
    else:
        inschrijvingen[ploeg].append(persoon)
    return inschrijvingen