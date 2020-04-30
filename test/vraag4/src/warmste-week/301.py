def gift_inschrijven(sponsoringen, giften):
    klas, gift = sponsoringen
    if klas in giften:
        giften[klas] += gift
    else:
        giften[klas] = gift
    return giften