def gift_inschrijven(tuple, giften):
    klas = tuple[0]
    bedrag = tuple[1]
    if klas in giften:
        bestaand = giften[klas]
        bestaand += bedrag
        giften[klas] = bestaand
    else:
        giften[klas] = bedrag
    return giften