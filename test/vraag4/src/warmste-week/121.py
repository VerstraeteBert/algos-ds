def gift_inschrijven(sponsering, giften):
    klas, bedrag = sponsering
    if klas in giften:
        giften[klas] += bedrag
    else:
        giften[klas] = bedrag
    return giften