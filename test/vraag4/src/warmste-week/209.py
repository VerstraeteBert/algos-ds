def gift_inschrijven(klas, giften):
    if klas[0] not in giften:
        giften[klas[0]] = klas[1]
    else:
        giften[klas[0]] = float(giften[klas[0]]) + float(klas[1])
    return giften
