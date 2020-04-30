def verlaat_ploeg(naam, ploeg, woordenlijst):
    namen = woordenlijst[ploeg]
    if len(namen) == 1:
        del woordenlijst[ploeg]
    for voornaam in namen:
        if voornaam == naam:
            namen.remove(naam)
    return woordenlijst

def vervoegt_ploeg(naam, ploeg, woordenlijst):
    lijst = []
    if ploeg not in woordenlijst:
        lijst.append(naam)
        woordenlijst[ploeg] = lijst
    else:
        namen = woordenlijst[ploeg]
        namen.append(naam)
    return woordenlijst
