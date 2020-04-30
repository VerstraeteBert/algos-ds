def verlaat_ploeg(naam, ploeg, teams):
    teams[ploeg].remove(naam)
    if len(teams[ploeg]) == 0:
        teams.pop(ploeg)
    return teams

def vervoegt_ploeg(naam, ploeg, teams):
    if ploeg in teams:
        teams[ploeg].append(naam)
    else:
        teams.update({ploeg: [naam]})
    return teams