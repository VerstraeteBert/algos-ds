def verlaat_ploeg(persoon, ploeg, inschrijving):
    waarde = inschrijving[ploeg]
    waarde.remove(persoon)
    if waarde == []:
        del inschrijving[ploeg]
    else:
        inschrijving[ploeg] = waarde
    return inschrijving
def vervoegt_ploeg(persoon, ploeg, inschrijving):
    if ploeg in inschrijving:
        waarde = inschrijving[ploeg]
        waarde.append(persoon)
        inschrijving[ploeg] = waarde
    else:
        waarde = []
        waarde.append(persoon)
        inschrijving[ploeg] = waarde
    return inschrijving