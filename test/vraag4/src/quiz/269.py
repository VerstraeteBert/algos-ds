def verlaat_ploeg(naam, ploeg, wb):
    wb[ploeg].remove(naam)
    if not wb[ploeg]:
        del wb[ploeg]
    return wb

def vervoegt_ploeg(naam, ploeg, wb):
    if not ploeg in wb:
        wb[ploeg] = []
    if not naam in wb[ploeg]:
        wb[ploeg].append(naam)
    return wb