def verlaat_ploeg(naam, ploeg, woordenboek):
    woordenboek[ploeg].remove(naam)
    if woordenboek[ploeg] == []:
        del woordenboek[ploeg]
    return woordenboek

def vervoegt_ploeg(naam, ploeg, woordenboek ):
    if ploeg in woordenboek:
        woordenboek[ploeg].append(naam)
    else:
        woordenboek[ploeg] = naam.split()
    return woordenboek