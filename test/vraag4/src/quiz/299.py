def verlaat_ploeg(naam, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(naam)
    if not inschrijvingen[ploeg]: #als de key geen value heeft, mag je de key verwijderen
        del(inschrijvingen[ploeg])
    return inschrijvingen

def vervoegt_ploeg(naam, ploeg, inschrijvingen):
    if ploeg not in inschrijvingen.keys():
        inschrijvingen[ploeg]=[]
    inschrijvingen[ploeg].append(naam)
    return inschrijvingen