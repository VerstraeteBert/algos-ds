def gift_inschrijven(tuple, dictionnary):
    klas = tuple[0]
    if klas in dictionnary:
        dictionnary[klas] += tuple[1]
    else:
        dictionnary[klas] = tuple[1]
    return dictionnary