def verlaat_ploeg(naamweg, ploeg, ding):
    ding[ploeg].remove(naamweg)
    if not ding[ploeg]:
        del ding[ploeg]
    return ding

def vervoegt_ploeg(naambij, ploeg, ding):
    if not ploeg in ding:
        ding[ploeg] = [naambij]
    else:
        ding[ploeg].append(naambij)
    return ding
 