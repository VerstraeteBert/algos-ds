def verlaat_ploeg(naam, ploeg, woordenboek):
    woordenboek[ploeg].remove(naam)
    if len(woordenboek[ploeg]) == 0:
        del woordenboek[ploeg]
    return woordenboek
def vervoegt_ploeg(naam, ploeg, woordenboek):
    if ploeg not in woordenboek:
        woordenboek[ploeg] = [naam]
    else:
        woordenboek[ploeg].append(naam)
    return woordenboek