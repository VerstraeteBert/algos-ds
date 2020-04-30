def verlaat_ploeg(naam, team, dictio):
    teamleden = dictio[team]
    teamleden.remove(naam)
    if teamleden == []:
        del dictio[team]
    else:
        dictio[team] = teamleden
    return dictio
    
def vervoegt_ploeg(naam, team, dictio):
    if team in dictio:
        teamleden = dictio[team]
        teamleden.append(naam)
        dictio[team] = teamleden
    else:
        teamleden = [naam]
        dictio[team] = teamleden
    return dictio