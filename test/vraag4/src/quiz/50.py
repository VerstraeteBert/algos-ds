def verlaat_ploeg(verlater, ploeg, teams):
    if verlater in teams[ploeg]:
        teams[ploeg].remove(verlater)
    if not teams[ploeg]:
        del teams[ploeg]
    return teams

def vervoegt_ploeg(vervoeger, ploeg, teams):
    if ploeg not in teams:
        teams[ploeg] = []
    if vervoeger not in teams[ploeg]:
        teams[ploeg].append(vervoeger)

    return teams