def gift_inschrijven(klas_bedrag, giften):
    for klas in giften:
        if klas_bedrag[0] == klas:
            giften[klas] += klas_bedrag[1]
    if klas_bedrag[0] not in giften:
        giften[klas_bedrag[0]] = klas_bedrag[1]
    return giften


print(gift_inschrijven(('5IN', 73.81), {'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 232.48}))
