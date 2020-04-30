def gift_inschrijven(klas,dictionary):
    if klas[0] in dictionary:
        dictionary[klas[0]]+=klas[1]
    else:
        dictionary.update({klas[0]:klas[1]})
    return dictionary