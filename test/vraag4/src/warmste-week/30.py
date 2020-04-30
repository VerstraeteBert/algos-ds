def gift_inschrijven(klas, giften):
    bedrag = klas[1]
    klas = klas[0]
    if klas in giften:
        giften[klas] += bedrag
    else:
        giften[klas] = bedrag
    return giften