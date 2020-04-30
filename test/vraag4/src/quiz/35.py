def verlaat_ploeg(naam, ploeg, totaal):
    leden = totaal[ploeg]
    leden.remove(naam)
    if leden == []:
        del totaal[ploeg]
    else:
        totaal[ploeg] = leden
    return totaal


def vervoegt_ploeg(naam, ploeg, totaal):
    x = []
    if ploeg in totaal:
        leden = totaal[ploeg]
        leden.append(naam)
        totaal[ploeg] = leden
    else:
        x.append(naam)
        totaal[ploeg] = x
    return totaal