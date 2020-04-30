def verlaat_ploeg(naam, team, woordenboek):
    woordenboek[team].remove(naam)
    if not woordenboek[team]:
        del woordenboek[team]
    return woordenboek

def vervoegt_ploeg(naam, team, woordenboek):
    if not team in woordenboek:
        woordenboek[team] = []
    if not naam in woordenboek[team]:
        woordenboek[team].append(naam)
    return woordenboek