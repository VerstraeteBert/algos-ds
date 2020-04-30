def gift_inschrijven(sponsering, giften):
    klas, gift = sponsering
    if klas not in giften:
        giften[klas] = 0
    giften[klas] += gift
    return giften