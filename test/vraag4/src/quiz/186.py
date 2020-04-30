def verlaat_ploeg(naam, ploeg, leden):
    leden[ploeg].remove(naam)
    if not leden[ploeg]:
        del leden[ploeg]
    return leden
    
def vervoegt_ploeg(naam, ploeg, leden):
    if not ploeg in leden:
        leden[ploeg] = []
    if not naam in ploeg:
        leden[ploeg].append(naam)
    return leden
    