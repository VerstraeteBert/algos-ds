def verlaat_ploeg(naam,ploeg,woordenboek):
    woordenboek[ploeg].remove(naam)
    if not woordenboek[ploeg]:
        del woordenboek[ploeg]
    return woordenboek

def vervoegt_ploeg(naam,ploeg,woordenboek):
    if not ploeg in woordenboek:
        woordenboek[ploeg] = []
    if not naam in woordenboek[ploeg]:
        woordenboek[ploeg].append(naam)
    return woordenboek