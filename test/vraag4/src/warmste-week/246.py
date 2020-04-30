def gift_inschrijven(sponsoring, giften):
    klas, bedrag= sponsoring
    if klas in giften:
        giften[klas] += bedrag
    else:
        giften[klas] = bedrag
    return giften