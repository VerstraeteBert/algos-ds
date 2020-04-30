def gift_inschrijven(bedrag, giften):
    klas, gift = bedrag
    if not klas in giften:
        giften[klas] = 0
    giften[klas] += gift
    return giften
