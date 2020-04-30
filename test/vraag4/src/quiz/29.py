def verlaat_ploeg(naam, ploeg, woordenboek):
    woordenboek[ploeg].remove(naam)
    if not woordenboek[ploeg]:
        del woordenboek[ploeg]
    return woordenboek
def vervoegt_ploeg(naam, ploeg, woordenboek):
    if ploeg in woordenboek and naam not in woordenboek[ploeg]:
        woordenboek[ploeg].append(naam)
    elif ploeg not in woordenboek:
        woordenboek[ploeg] = [naam]
    return woordenboek