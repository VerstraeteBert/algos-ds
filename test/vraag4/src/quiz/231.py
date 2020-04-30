def verlaat_ploeg(deelnemer, ploeg, woordenboek):
    woordenboek[ploeg].remove(deelnemer)
    if not woordenboek[ploeg]:
        del woordenboek[ploeg]
    return woordenboek

def vervoegt_ploeg(naam, ploeg, deelnemers):
    if not ploeg in deelnemers:
        deelnemers[ploeg] = []
    if not naam in deelnemers[ploeg]:
        deelnemers[ploeg].append(naam)
    return deelnemers
