def verlaat_ploeg(speler, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(speler)
    lege_key = [k for k, v in inschrijvingen.items() if not v]
    for k in lege_key:
        del inschrijvingen[k]
    return inschrijvingen


def vervoegt_ploeg(naam, ploeg, lijst_ploegen):
    if ploeg not in lijst_ploegen:
        lijst_ploegen[ploeg] = [naam]
    elif naam not in lijst_ploegen[ploeg]:
        lijst_ploegen[ploeg].append(naam)
    return lijst_ploegen