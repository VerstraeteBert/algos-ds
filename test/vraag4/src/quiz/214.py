def verlaat_ploeg(speler, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(speler)
    lege_key = [k for k, v in inschrijvingen.items() if not v]
    for k in lege_key:
        del inschrijvingen[k]
    return inschrijvingen


def vervoegt_ploeg(speler, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        inschrijvingen[ploeg].append(speler)
    else:
        inschrijvingen[ploeg] = [speler]
    return inschrijvingen