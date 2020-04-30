def gift_inschrijven(sponsor, giften):
    klas, gift = sponsor
    if klas not in giften:
        giften[klas] = 0
    giften[klas] += gift
    return giften
