def verlaat_ploeg(verlater, ploeg, woordenboek):
    if ploeg in woordenboek:
        woordenboek[ploeg].remove(verlater)
    if not woordenboek[ploeg]:
        del woordenboek[ploeg]

    return woordenboek



def vervoegt_ploeg(joiner, ploeg, woordenboek):
    if ploeg in woordenboek:
        woordenboek[ploeg].append(joiner)

    elif ploeg not in woordenboek:
        woordenboek[ploeg] = []
        woordenboek[ploeg].append(joiner)

    return woordenboek