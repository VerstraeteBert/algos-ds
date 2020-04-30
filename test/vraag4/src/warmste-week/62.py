def gift_inschrijven(sponsering, giften):
    klas, gift = sponsering
    if klas in giften:
        giften[klas] += gift
    else:
        giften[klas] = gift
    return giften