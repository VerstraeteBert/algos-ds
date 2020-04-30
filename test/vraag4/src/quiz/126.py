def verlaat_ploeg(naam, team, woordenboek):
    if team in woordenboek:
        lijst=woordenboek[team]
        lijst.remove(naam)
        if len(lijst)==0:
            del woordenboek[team]
    return woordenboek

def vervoegt_ploeg(naam, team, woordenboek):
    if team in woordenboek:
        lijst=woordenboek[team]
        x=(len(lijst))
        lijst.insert(x, naam)
    else:
        list=[naam]
        woordenboek[team] = list
    return woordenboek
