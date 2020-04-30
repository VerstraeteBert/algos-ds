def verlaat_ploeg(naam_verlater, ploeg, dictionary_inschrijvingen):
    lijst_van_ploeg = dictionary_inschrijvingen[ploeg]
    lijst_van_ploeg.remove(naam_verlater)
    if lijst_van_ploeg == []:
        del dictionary_inschrijvingen[ploeg]
    else:
        dictionary_inschrijvingen[ploeg] = lijst_van_ploeg
    return dictionary_inschrijvingen


def vervoegt_ploeg(naam, ploeg, dictionary_inschrijvingen):
    if ploeg in dictionary_inschrijvingen:
        lijst_van_ploeg = dictionary_inschrijvingen[ploeg]
        lijst_van_ploeg.append(naam)
        dictionary_inschrijvingen[ploeg] = lijst_van_ploeg
    else:
        dictionary_inschrijvingen[ploeg] = [naam]
    return dictionary_inschrijvingen