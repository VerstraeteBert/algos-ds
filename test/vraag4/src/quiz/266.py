def verlaat_ploeg(naam, ploeg, woordenboek):
    correctie = woordenboek[ploeg]
    correctie.remove(naam)
    if len(correctie) != 0:
        woordenboek[ploeg] = correctie
    else:
        woordenboek.pop(ploeg, None)
    return woordenboek

def vervoegt_ploeg(naam, ploeg, woordenboek):
    if ploeg in woordenboek:
        correctie = woordenboek[ploeg]
        correctie.append(naam)
        woordenboek[ploeg] = correctie
    else:
        woordenboek[ploeg] = [naam]
    return woordenboek
    