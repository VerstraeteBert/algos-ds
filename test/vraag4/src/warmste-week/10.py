def gift_inschrijven(sponsoring,giftenlijst):
    klas, gift = sponsoring
    if klas in giftenlijst:
        giftenlijst[klas] += gift
    else:
        giftenlijst[klas] = gift
    return giftenlijst
