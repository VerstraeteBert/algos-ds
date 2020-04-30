def verlaat_ploeg(deelnemer, ploeg, woordenboek):
    woordenboek[ploeg].remove(deelnemer)
    if not woordenboek[ploeg]:
        del woordenboek[ploeg]
    return woordenboek

def vervoegt_ploeg(deelnemer, ploeg, woordenboek):
    if not ploeg in woordenboek:
        woordenboek[ploeg] = []
    woordenboek[ploeg].append(deelnemer)
    return woordenboek