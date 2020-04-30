def verlaat_ploeg(naam, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        namenlijst = inschrijvingen[ploeg]
        namenlijst.pop(namenlijst.index(naam))
    if not inschrijvingen[ploeg]:
        del inschrijvingen[ploeg]
    return inschrijvingen
def vervoegt_ploeg(naam, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        namenlijst = inschrijvingen[ploeg]
        namenlijst += [naam]
    else:
        inschrijvingen[ploeg] = [naam]
    return inschrijvingen