def gift_inschrijven(sponsoring, samen):
    klas, gift = sponsoring
    if not klas in samen:
        samen[klas] = 0
    samen[klas] += gift
    return samen