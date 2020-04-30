def verlaat_ploeg(deelnemer, ploeg, diction):
    diction[ploeg].remove(deelnemer)
    if diction[ploeg] == []:
        del diction[ploeg]
    return diction
    
def vervoegt_ploeg(deelnemer, ploeg, diction):
    if not ploeg in diction:
        diction[ploeg] = []
    if not deelnemer in diction[ploeg]:
        diction[ploeg].append(deelnemer)
    return diction