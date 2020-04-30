def verlaat_ploeg(verlater, ploeg, woordenboek):
    lijst_ploeg = woordenboek[ploeg]
    lijst_ploeg.remove(verlater)
    if lijst_ploeg == []:
        woordenboek.pop(ploeg)
    else:
        woordenboek[ploeg] = lijst_ploeg
    return woordenboek

def vervoegt_ploeg(vervoeger, ploeg, woordenboek):
    if ploeg not in woordenboek:
        woordenboek[ploeg] = [vervoeger]
    else:
        lijst_ploeg = woordenboek[ploeg]
        if vervoeger not in lijst_ploeg:
            lijst_ploeg.append(vervoeger)
        woordenboek[ploeg] = lijst_ploeg
    return woordenboek