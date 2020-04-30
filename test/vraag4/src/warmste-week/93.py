def gift_inschrijven(sponsoring,giften):
    klas, gift = sponsoring
    if klas not in giften:
        giften[klas] = gift
    else:
        giften[klas] = giften[klas] + gift
    return giften
    