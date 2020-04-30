def verlaat_ploeg(naam, ploeg, inschrijvingen):
    ploeg2 = inschrijvingen[ploeg]
    if naam in ploeg2:
        ploeg2.remove(naam)
        if ploeg2 == []:
            del inschrijvingen[ploeg]
        return inschrijvingen
    else:
        return inschrijvingen
def vervoegt_ploeg(naam, ploeg, inschrijvingen):
    if ploeg not in inschrijvingen:
        inschrijvingen[ploeg] = [naam]
        return inschrijvingen
    else:
        ploeg2 = inschrijvingen[ploeg]
        ploeg2.append(naam)
        return inschrijvingen