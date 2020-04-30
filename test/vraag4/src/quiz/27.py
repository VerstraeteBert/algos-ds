def verlaat_ploeg(naam, groep, woordenboek):
    woordenboek[groep].remove(naam)
    if not woordenboek[groep]:
        del woordenboek[groep]
    return woordenboek
    
def vervoegt_ploeg(naam, groep, woordenboek):
    if groep in woordenboek:
        woordenboek[groep] += [naam]
    else:
        woordenboek[groep] = [naam]
    return woordenboek