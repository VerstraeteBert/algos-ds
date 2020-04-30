def gift_inschrijven(klasgift, giften):
    klas, gift = klasgift
    if klas not in giften:
        giften[klas] = 0
    giften[klas] += gift
    return giften
