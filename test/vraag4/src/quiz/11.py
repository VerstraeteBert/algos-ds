def verlaat_ploeg(naam, ploeg, teams):
    teams[ploeg].remove(naam)
    if not teams[ploeg]:
        del teams[ploeg]
    return teams


def vervoegt_ploeg(naam, ploeg, teams):
    if ploeg not in teams:
        teams[ploeg] = []
    if naam not in teams[ploeg]:
        teams[ploeg].append(naam)
    return teams
