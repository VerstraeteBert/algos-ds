def verlaat_ploeg(naam, ploeg, woordenboek):
    woordenboek[ploeg].remove(naam)
    if len(woordenboek[ploeg]) == 0:
        woordenboek.pop(ploeg)
    return woordenboek

def vervoegt_ploeg(naam, ploeg, woordenboek): 
    if woordenboek.get(ploeg) == None:
        woordenboek[ploeg] = []
    woordenboek[ploeg].append(naam)
    return woordenboek