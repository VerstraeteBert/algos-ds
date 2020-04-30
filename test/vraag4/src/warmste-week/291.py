def gift_inschrijven(klas_bedrag, bedragen_dictionary):
    if klas_bedrag[0] in bedragen_dictionary:
        bedragen_dictionary[klas_bedrag[0]] = bedragen_dictionary.get(klas_bedrag[0]) + klas_bedrag[1]
    else:
        bedragen_dictionary[klas_bedrag[0]] = klas_bedrag[1]
    return bedragen_dictionary