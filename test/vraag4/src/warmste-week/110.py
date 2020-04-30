def gift_inschrijven(sponsoring, giften): #sponsering = tuple met (klas, gift) en giften = dictionary
    klas, gift = sponsoring
    if not klas in giften:
        giften[klas] = gift #key van dictionary
    else:
        giften[klas] += gift
    return giften

