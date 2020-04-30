def gift_inschrijven(info, giften):
    klas, bedrag = info
    if klas not in giften:
        giften[klas] = 0
    giften[klas] += bedrag     
    return giften