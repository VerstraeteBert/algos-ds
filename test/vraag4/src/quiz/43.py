def verlaat_ploeg(naam, ploegnaam, woordenboek):
    een_waarde = woordenboek[ploegnaam]
    een_waarde.remove(naam)
    if len(een_waarde) == 0:
        woordenboek.pop(ploegnaam)
    return woordenboek
def vervoegt_ploeg(naam, ploegnaam, woordenboek):
    if ploegnaam not in woordenboek:
        woordenboek[ploegnaam] = [naam]
    else:
        eenwaarde = woordenboek[ploegnaam]
        eenwaarde.append(naam)
    return woordenboek
    