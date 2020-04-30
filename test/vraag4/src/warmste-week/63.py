def gift_inschrijven(sponsoring, giften):
    klas, gift = sponsoring
    if klas in giften:
        giften[klas] += gift
    else:
        giften[klas] = gift 
    return giften