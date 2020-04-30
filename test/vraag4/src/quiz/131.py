def verlaat_ploeg(naam, ploeg, inschrijving):
    p = inschrijving[ploeg]
    p.remove(naam)
    inschrijving[ploeg] = p
    if p == []:
        del inschrijving[ploeg]
    return inschrijving

def vervoegt_ploeg(naam, ploeg, inschrijving):
    if not ploeg in inschrijving.keys():
        inschrijving[ploeg] = [naam]
    else:
        p = inschrijving[ploeg]
        p.append(naam)
        inschrijving[ploeg] = p
    return inschrijving