def verlaat_ploeg(deelnemer, ploeg, inschrijvingen_dictionary):
    deelnemers_ploeg = inschrijvingen_dictionary.get(ploeg)
    index = deelnemers_ploeg.index(ploeg)
    deelnemers_ploeg.remove(deelnemer)
    if deelnemers_ploeg == []:
        inschrijvingen_dictionary.pop(index)
        return inschrijvingen_dictionary
    else:
        inschrijvingen_dictionary[ploeg] = deelnemers_ploeg
        return inschrijvingen_dictionary