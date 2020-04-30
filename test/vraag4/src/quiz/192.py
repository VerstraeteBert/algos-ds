def verlaat_ploeg(deelnemer, ploeg, inschrijvingen):
    inschrijvingen_edit = inschrijvingen
    inschrijvingen_edit[ploeg].pop(inschrijvingen_edit[ploeg].index(deelnemer))
    if len(inschrijvingen_edit[ploeg]) == 0:
        del inschrijvingen_edit[ploeg]
    return inschrijvingen_edit


def vervoegt_ploeg(deelnemer, ploeg, inschrijvingen):
    inschrijvingen_edit = inschrijvingen
    if ploeg not in inschrijvingen_edit:
        inschrijvingen_edit[ploeg] = []
    inschrijvingen_edit[ploeg].append(deelnemer)

    return inschrijvingen_edit



