def verlaat_ploeg(naam, team, woordenboek):
    l = woordenboek[team]
    l.remove(naam)
    if len(l) == 0:
        woordenboek.pop(team)
    else:
        woordenboek[team] = l
    return woordenboek

def vervoegt_ploeg(naam, team, woordenboek):
    if team in woordenboek:
        l = woordenboek[team]
        l.append(naam)
        woordenboek[team] = l
    else:
        woordenboek[team] = [naam]
    return woordenboek
        
    
    